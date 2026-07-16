#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 || -z "$1" ]]; then
  echo "Usage: $0 <process-query>" >&2
  exit 2
fi

query=$1
pids=$(pgrep -f -- "$query" || true)

if [[ -z "$pids" ]]; then
  echo "No process matched: $query" >&2
  exit 1
fi

while IFS= read -r pid; do
  command=$(ps -p "$pid" -o command=)
  thread_count=$(ps -M "$pid" | tail -n +2 | wc -l | tr -d ' ')
  printf 'PID=%s threads=%s command=%s\n' "$pid" "$thread_count" "$command"
done <<< "$pids"
