#!/bin/bash
# Wait for any in-flight run_chunks.sh to finish, then start the next range.
#
#   nohup caffeinate -i ./queue_run.sh 6 10 > queued.out 2>&1 &
#
# Two runs must never overlap: they append to the same ledger, rebuild the same
# parquets and commit against the same git index. This blocks until the current
# one exits, then takes over.

set -uo pipefail
FROM=${1:?usage: queue_run.sh FROM TO}
TO=${2:?usage: queue_run.sh FROM TO}
REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

waited=0
while pgrep -f "run_chunks\.sh" >/dev/null 2>&1; do
  if [ "$waited" -eq 0 ]; then
    echo "$(date +%H:%M) a run is in progress; waiting for it to finish before starting $FROM..$TO"
  fi
  sleep 60
  waited=$((waited+1))
  [ $((waited % 10)) -eq 0 ] && echo "$(date +%H:%M) still waiting (${waited}m)"
done
[ "$waited" -gt 0 ] && echo "$(date +%H:%M) previous run finished after ${waited}m"

# If the run we waited for already covered part of this range, skip ahead.
DONE=$(grep -o '"chunk": *[0-9]*' data/annotated/annotations/family_assignments.jsonl \
       | grep -o '[0-9]*$' | sort -n | tail -1)
if [ -n "$DONE" ] && [ "$DONE" -ge "$FROM" ]; then
  echo "$(date +%H:%M) chunks up to $DONE are already annotated; starting at $((DONE+1))"
  FROM=$((DONE+1))
fi
if [ "$FROM" -gt "$TO" ]; then
  echo "$(date +%H:%M) nothing left to do in that range."
  exit 0
fi

echo "$(date +%H:%M) starting chunks $FROM..$TO"
exec ./run_chunks.sh "$FROM" "$TO"
