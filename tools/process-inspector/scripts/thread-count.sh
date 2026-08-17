#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 || -z "$1" ]]; then
  echo "Usage: $0 <process-query>" >&2
  exit 2
fi

query=$1
if pids=$(pgrep -f -- "$query"); then
  :
else
  status=$?
  if [[ $status -eq 1 ]]; then
    echo "No process matched: $query" >&2
  else
    echo "Failed to search for processes: $query" >&2
  fi
  exit "$status"
fi

if [[ -z "$pids" ]]; then
  echo "No process matched: $query" >&2
  exit 1
fi

reported=0
first_failure_status=0
while IFS= read -r pid; do
  [[ -n $pid ]] || continue
  if command=$(ps -p "$pid" -o command=); then
    :
  else
    status=$?
    if [[ $first_failure_status -eq 0 ]]; then
      first_failure_status=$status
    fi
    printf 'Skipping PID %s: failed to read command\n' "$pid" >&2
    continue
  fi
  if thread_snapshot=$(ps -M "$pid"); then
    :
  else
    status=$?
    if [[ $first_failure_status -eq 0 ]]; then
      first_failure_status=$status
    fi
    printf 'Skipping PID %s: failed to read threads\n' "$pid" >&2
    continue
  fi
  thread_count=$(awk 'NR > 1 { count += 1 } END { print count + 0 }' <<<"$thread_snapshot")
  printf 'PID=%s threads=%s command=%s\n' "$pid" "$thread_count" "$command"
  ((reported += 1))
done <<<"$pids"

if [[ $reported -eq 0 ]]; then
  echo "No matched process remained available: $query" >&2
  if [[ $first_failure_status -ne 0 ]]; then
    exit "$first_failure_status"
  fi
  exit 1
fi

exit 0
