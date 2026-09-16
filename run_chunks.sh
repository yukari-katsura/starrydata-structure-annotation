#!/bin/bash
# Annotate a range of chunks unattended, stopping at the first sign of trouble.
#
#   caffeinate -i ./run_chunks.sh 5 10
#
# caffeinate -i holds an idle-sleep assertion for this script's lifetime and
# releases it on exit. Display and disk sleep are harmless and left alone.
#
# One `claude -p` invocation per chunk rather than one for the whole range:
# each chunk is a bounded task, the gate runs between them, and a failure stops
# the loop with everything before it already committed.

set -uo pipefail
FROM=${1:?usage: run_chunks.sh FROM TO}
TO=${2:?usage: run_chunks.sh FROM TO}
REPO="$(cd "$(dirname "$0")" && pwd)"
PY="${PY:-python}"
LOG="$REPO/run_chunks.$(date +%Y%m%d-%H%M).log"
cd "$REPO"

echo "annotating chunks $FROM..$TO, logging to $LOG"
for n in $(seq "$FROM" "$TO"); do
  CH=$(printf '%03d' "$n")
  echo "=== chunk $CH  $(date +%H:%M) ===" | tee -a "$LOG"

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
    >>"$LOG" 2>&1
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "claude exited $rc on chunk $CH -- stopping" | tee -a "$LOG"; exit 1
  fi

  # rebuild derived tables, then gate
  $PY scripts/add_assignment_ids.py        >>"$LOG" 2>&1
  $PY scripts/apply_composition_splits.py  >>"$LOG" 2>&1
  $PY scripts/add_assignment_ids.py        >>"$LOG" 2>&1
  $PY scripts/build_annotated_samples.py   >>"$LOG" 2>&1

  if ! $PY scripts/verify_assignments.py --quiet | tee -a "$LOG"; then
    echo "GATE FAILED after chunk $CH -- stopping, nothing committed" | tee -a "$LOG"
    exit 1
  fi
  $PY scripts/verify_assignments.py --apply --quiet >>"$LOG" 2>&1
  $PY scripts/build_annotated_samples.py            >>"$LOG" 2>&1

  git add -A && git commit -q -m "Annotate chunk $CH (unattended run)" \
    && echo "chunk $CH committed" | tee -a "$LOG"
done

$PY scripts/build_review_queue.py | tee -a "$LOG"
echo "done $(date +%H:%M). Nothing pushed -- review, then git push." | tee -a "$LOG"
