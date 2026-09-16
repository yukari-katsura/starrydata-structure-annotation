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
PY="${PY:-python}"
STAMP=$(date +%Y%m%d-%H%M)
LOG="$REPO/run_chunks.$STAMP.log"
LEDGER="$REPO/data/annotated/annotations/family_assignments.jsonl"
cd "$REPO"

# Stop when the five-hour window is this full. Leaving headroom matters: a chunk
# takes ~20 minutes, so starting one at 95% means it dies partway rather than
# not starting.
QUOTA_STOP=${QUOTA_STOP:-0.85}
MIN_RECORDS=${MIN_RECORDS:-40}   # a chunk is 50 hosts; well short means it failed

say() { echo "$*" | tee -a "$LOG"; }
say "annotating chunks $FROM..$TO, log: $LOG"

for n in $(seq "$FROM" "$TO"); do
  CH=$(printf '%03d' "$n")
  RAW="$REPO/run_chunks.$STAMP.chunk$CH.jsonl"
  before=$(wc -l < "$LEDGER" | tr -d ' ')
  say "=== chunk $CH  $(date +%H:%M)  (ledger: $before) ==="

  # stdin redirected: without it claude -p waits 3s for input that never comes.
  # stream-json so the log grows during the chunk -- otherwise a hung run and a
  # working one look identical for twenty minutes.
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
    < /dev/null > "$RAW" 2>&1
  rc=$?

  # what the run reported about itself
  eval "$($PY - "$RAW" <<'PYEOF'
import json, sys
util=util7=None; ok=None; err=None
for line in open(sys.argv[1], errors='replace'):
    line=line.strip()
    if not line.startswith('{'): continue
    try: d=json.loads(line)
    except Exception: continue
    if d.get('type')=='rate_limit_event':
        w=d.get('rate_limit_info',{}).get('unifiedWindows',{})
        util=w.get('five_hour',{}).get('utilization', util)
        util7=w.get('seven_day',{}).get('utilization', util7)
    if d.get('type')=='result':
        ok = not d.get('is_error'); err=d.get('subtype')
print(f'UTIL={util if util is not None else -1}')
print(f'UTIL7={util7 if util7 is not None else -1}')
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

  # Stop before the window empties rather than dying partway through a chunk.
  if [ "$UTIL" != "-1" ] && $PY -c "import sys; sys.exit(0 if float('$UTIL')>=float('$QUOTA_STOP') else 1)"; then
    say "  quota window at ${UTIL} (stop threshold $QUOTA_STOP) -- stopping cleanly after chunk $CH."
    say "  Resume later with: ./run_chunks.sh $((n+1)) $TO"
    exit 0
  fi
done

$PY scripts/build_review_queue.py | tee -a "$LOG"
say "done $(date +%H:%M). Committed locally, nothing pushed."
