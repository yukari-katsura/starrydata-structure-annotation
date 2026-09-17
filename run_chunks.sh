#!/bin/bash
# Annotate a range of chunks unattended, stopping at the first sign of trouble.
#
#   caffeinate -i ./run_chunks.sh 5 10
#
# Run this from your own terminal, NOT from inside a Claude Code session: a
# session running this spawns a second Claude that also draws on your quota,
# and contributes nothing while the subprocess works.
#
# caffeinate -i holds an idle-sleep assertion for this script's lifetime and
# releases it on exit. Display and disk sleep do not stop computation.

set -uo pipefail
FROM=${1:?usage: run_chunks.sh FROM TO}
TO=${2:?usage: run_chunks.sh FROM TO}
REPO="$(cd "$(dirname "$0")" && pwd)"
# Find an interpreter that actually has the dependencies. The repo has no venv
# of its own and `python` is not on PATH on this machine, so defaulting to it
# would fail only after a chunk had already been annotated -- twenty minutes in.
find_py() {
  local c
  for c in "${PY:-}" "$REPO/.venv/bin/python" \
           "$(dirname "$REPO")/starrydata-explorer/.venv/bin/python" \
           python3 python; do
    [ -n "$c" ] || continue
    command -v "$c" >/dev/null 2>&1 || [ -x "$c" ] || continue
    if "$c" -c "import pandas, pymatgen, openpyxl" >/dev/null 2>&1; then
      echo "$c"; return 0
    fi
  done
  return 1
}
if ! PY=$(find_py); then
  echo "No Python with pandas, pymatgen and openpyxl found." >&2
  echo "Set PY to one explicitly:  PY=/path/to/python ./run_chunks.sh $*" >&2
  exit 1
fi
STAMP=$(date +%Y%m%d-%H%M)
LOG="$REPO/run_chunks.$STAMP.log"
LEDGER="$REPO/data/annotated/annotations/family_assignments.jsonl"
cd "$REPO"

# Stop when the five-hour window is this full. Leaving headroom matters: a chunk
# takes ~20 minutes, so starting one at 95% means it dies partway rather than
# not starting.
QUOTA_STOP=${QUOTA_STOP:-0.85}
# stop | wait. "wait" sleeps until the five-hour window resets and carries on,
# for runs meant to span days. The seven-day window is never waited on: it
# recovers over days, not hours, so exhausting it ends the run.
QUOTA_MODE=${QUOTA_MODE:-stop}
QUOTA_7D_STOP=${QUOTA_7D_STOP:-0.90}
# optional wall-clock deadline, e.g. MAX_HOURS=36
MAX_HOURS=${MAX_HOURS:-0}
STARTED=$(date +%s)
MIN_RECORDS=${MIN_RECORDS:-40}   # a chunk is 50 hosts; well short means it failed

say() { echo "$*" | tee -a "$LOG"; }
say "annotating chunks $FROM..$TO"
say "  python: $PY"
say "  log:    $LOG"

for n in $(seq "$FROM" "$TO"); do
  CH=$(printf '%03d' "$n")
  RAW="$REPO/run_chunks.$STAMP.chunk$CH.jsonl"
  before=$(wc -l < "$LEDGER" | tr -d ' ')
  say "=== chunk $CH  $(date +%H:%M)  (ledger: $before) ==="

  # stdin redirected: without it claude -p waits 3s for input that never comes.
  # stream-json is piped through stream_progress.py so the terminal shows what
  # it is doing as it goes; the raw stream is kept by tee for later inspection.
  claude -p "Annotate chunk $CH following the process in data/annotated/README.md.
Read data/annotated/input/chunks/chunk_$CH.md, assign a structure prototype to
every host system in it, and append one record per host to
data/annotated/annotations/family_assignments.jsonl.

Rules:
- experimentally_confirmed stays false: these are candidate structures.
- Propose a new prototype in taxonomy/prototypes_proposed.jsonl before using it.
- Do not invent mp_ids; take them from the ref lines or leave them null.
- Where the references disagree with you, say so in the record rather than
  quietly matching them.
- Stop and report if the chunk file is missing or already annotated." \
    --permission-mode acceptEdits \
    --output-format stream-json --verbose \
    < /dev/null 2>&1 | tee "$RAW" | "$PY" scripts/stream_progress.py
  # tee and the filter are the last commands in the pipeline, so $? is theirs.
  # PIPESTATUS[0] is what claude actually returned.
  rc=${PIPESTATUS[0]}

  # what the run reported about itself
  eval "$($PY - "$RAW" <<'PYEOF'
import json, sys
util=util7=None; ok=None; err=None; resets=None
for line in open(sys.argv[1], errors='replace'):
    line=line.strip()
    if not line.startswith('{'): continue
    try: d=json.loads(line)
    except Exception: continue
    if d.get('type')=='rate_limit_event':
        w=d.get('rate_limit_info',{}).get('unifiedWindows',{})
        util=w.get('five_hour',{}).get('utilization', util)
        util7=w.get('seven_day',{}).get('utilization', util7)
        resets=w.get('five_hour',{}).get('resetsAt', resets)
    if d.get('type')=='result':
        ok = not d.get('is_error'); err=d.get('subtype')
print(f'UTIL={util if util is not None else -1}')
print(f'UTIL7={util7 if util7 is not None else -1}')
print(f'RESETS={resets or 0}')
print(f'OK={1 if ok else 0}')
print(f'SUBTYPE={err or "none"}')
PYEOF
)"

  say "  claude rc=$rc subtype=$SUBTYPE  quota: 5h=${UTIL} 7d=${UTIL7}"

  if [ "$rc" -ne 0 ] || [ "$OK" != "1" ]; then
    say "  claude failed (rc=$rc, subtype=$SUBTYPE) -- stopping. Nothing committed for $CH."
    exit 1
  fi

  # A quota limit, a refusal and a crash all look the same from outside: the
  # ledger did not grow. One test catches all of them.
  after=$(wc -l < "$LEDGER" | tr -d ' ')
  grew=$(( after - before ))
  if [ "$grew" -lt "$MIN_RECORDS" ]; then
    say "  chunk $CH added only $grew records (expected ~50) -- stopping."
    say "  Check $RAW for what it reported."
    exit 1
  fi
  say "  +$grew records"

  $PY scripts/add_assignment_ids.py        >>"$LOG" 2>&1
  $PY scripts/apply_composition_splits.py  >>"$LOG" 2>&1
  $PY scripts/add_assignment_ids.py        >>"$LOG" 2>&1
  $PY scripts/build_annotated_samples.py   >>"$LOG" 2>&1

  if ! $PY scripts/verify_assignments.py --quiet >>"$LOG" 2>&1; then
    say "  GATE FAILED after chunk $CH -- stopping, not committed."
    $PY scripts/verify_assignments.py --quiet | tail -20 | tee -a "$LOG"
    exit 1
  fi
  $PY scripts/verify_assignments.py --apply --quiet >>"$LOG" 2>&1
  $PY scripts/build_annotated_samples.py            >>"$LOG" 2>&1

  git add -A && git commit -q -m "Annotate chunk $CH (unattended run)" && say "  committed"

  # The seven-day window recovers over days; there is no point waiting on it.
  if [ "$UTIL7" != "-1" ] && $PY -c "import sys; sys.exit(0 if float('$UTIL7')>=float('$QUOTA_7D_STOP') else 1)"; then
    say "  seven-day window at ${UTIL7} -- stopping. It recovers over days, not hours."
    say "  Resume later with: ./run_chunks.sh $((n+1)) $TO"
    exit 0
  fi

  if [ "$MAX_HOURS" != "0" ]; then
    elapsed_h=$(( ($(date +%s) - STARTED) / 3600 ))
    if [ "$elapsed_h" -ge "$MAX_HOURS" ]; then
      say "  reached MAX_HOURS=$MAX_HOURS -- stopping after chunk $CH."
      say "  Resume later with: ./run_chunks.sh $((n+1)) $TO"
      exit 0
    fi
  fi

  # Stop before the window empties rather than dying partway through a chunk.
  if [ "$UTIL" != "-1" ] && $PY -c "import sys; sys.exit(0 if float('$UTIL')>=float('$QUOTA_STOP') else 1)"; then
    if [ "$QUOTA_MODE" != "wait" ]; then
      say "  quota window at ${UTIL} (stop threshold $QUOTA_STOP) -- stopping cleanly after chunk $CH."
      say "  Resume later with: ./run_chunks.sh $((n+1)) $TO"
      exit 0
    fi
    now=$(date +%s)
    # +120s of slack: resuming exactly on the boundary tends to find the window
    # not yet credited.
    target=$(( ${RESETS:-0} + 120 ))
    if [ "$target" -le "$now" ]; then target=$(( now + 900 )); fi
    wait_s=$(( target - now ))
    say "  quota window at ${UTIL}; waiting $(( wait_s / 60 )) min for it to reset "\
        "($(date -r "$target" +%H:%M 2>/dev/null || date -d "@$target" +%H:%M))"
    while [ "$(date +%s)" -lt "$target" ]; do
      sleep 300
      left=$(( (target - $(date +%s)) / 60 ))
      [ "$left" -gt 0 ] && echo "    …$left min until the window resets" || true
    done
    say "  window reset -- continuing with chunk $((n+1))"
  fi

  # Raw streams are 5-10 MB each; a long run would otherwise fill the disk.
  gzip -f "$RAW" 2>/dev/null || true
done

$PY scripts/build_review_queue.py | tee -a "$LOG"
say "done $(date +%H:%M). Committed locally, nothing pushed."
