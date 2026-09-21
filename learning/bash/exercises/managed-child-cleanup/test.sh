#!/usr/bin/env bash

set -euo pipefail

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  if [[ -n ${state_dir:-} ]]; then
    for log in "$state_dir/stdout" "$state_dir/stderr"; do
      if [[ -s $log ]]; then
        printf '%s:\n' "$log" >&2
        head -c 4096 "$log" >&2
      fi
    done
  fi
  exit 1
}

run_isolated() {
  [[ $# == 1 && -f $1 && -r $1 ]] || fail "usage: bash $0 IMPLEMENTATION_PATH"
  if [[ -z ${JADE_BASH_IMAGE:-} || -z ${JADE_BASH_VERSION:-} ]]; then
    command -v mise >/dev/null || fail 'mise is required for the pinned runtime'
    exec mise exec -- bash "$0" "$@"
  fi
  command -v docker >/dev/null || fail 'Docker is required'
  local test_dir implementation
  test_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
  implementation=$(cd -- "$(dirname -- "$1")" && printf '%s/%s' "$PWD" "$(basename -- "$1")")
  # Docker's --mount parser treats commas as separators, even inside quoted paths.
  [[ $test_dir != *,* && $implementation != *,* ]] || fail 'mount paths cannot contain commas'
  exec docker run --rm --init --network none --read-only \
    --cap-drop ALL --security-opt no-new-privileges \
    --pids-limit 64 --memory 128m --cpus 1 \
    --tmpfs /tmp:rw,nosuid,nodev,size=16m \
    --mount "type=bind,source=$test_dir,target=/tests,readonly" \
    --mount "type=bind,source=$implementation,target=/candidate.sh,readonly" \
    -e JADE_CLEANUP_TEST_INSIDE=1 -e "EXPECTED_BASH_VERSION=$JADE_BASH_VERSION" \
    --entrypoint timeout "$JADE_BASH_IMAGE" \
    -s KILL 20 bash /tests/test.sh --inside
}

running() {
  local pid=$1 key value rest
  [[ -r /proc/$pid/status ]] || return 1
  while read -r key value rest; do
    if [[ $key == State: ]]; then
      [[ $value != Z && $value != X ]]
      return
    fi
  done <"/proc/$pid/status"
  return 1
}

await_ready() {
  local attempt
  for ((attempt = 0; attempt < 150; attempt++)); do
    [[ ! -f $state_dir/ready ]] || return 0
    running "$parent" || fail "$scenario: parent exited before ready"
    sleep 0.02
  done
  fail "$scenario: readiness timeout"
}

validate_child() {
  local pid=$1 key value rest ppid='' comm
  [[ $pid =~ ^[1-9][0-9]*$ ]] || fail "$scenario: invalid child PID"
  [[ -r /proc/$pid/status ]] || fail "$scenario: child missing at readiness"
  while read -r key value rest; do
    [[ $key != PPid: ]] || ppid=$value
  done <"/proc/$pid/status"
  [[ $ppid == "$parent" ]] || fail "$scenario: PID $pid is not a direct child"
  read -r comm <"/proc/$pid/comm"
  [[ $comm == sleep ]] || fail "$scenario: child must be a direct sleep process"
  running "$pid" || fail "$scenario: child not running at readiness"
}

await_exit() {
  local pid=$1 attempt
  for ((attempt = 0; attempt < 250; attempt++)); do
    if ! running "$pid"; then
      return 0
    fi
    sleep 0.02
  done
  fail "$scenario: PID $pid did not finish within 5 seconds"
}

run_case() {
  local scenario=$1 first_duration=$2 second_duration=$3 expected=$4
  local state_dir parent first second status start elapsed sentinel
  local -a manifest
  state_dir=$(mktemp -d "/tmp/$scenario space.XXXXXX")
  sleep 30 &
  sentinel=$!
  start=$SECONDS
  bash /candidate.sh "$state_dir" "$first_duration" "$second_duration" \
    >"$state_dir/stdout" 2>"$state_dir/stderr" &
  parent=$!
  await_ready
  [[ -f $state_dir/children.tsv ]] || fail "$scenario: missing children.tsv"
  mapfile -t manifest <"$state_dir/children.tsv"
  [[ ${#manifest[@]} == 2 ]] || fail "$scenario: expected exactly two child rows"
  [[ ${manifest[0]} == first$'\t'* && ${manifest[1]} == second$'\t'* ]] || fail "$scenario: invalid task names"
  first=${manifest[0]#*$'\t'}
  second=${manifest[1]#*$'\t'}
  [[ $first != "$second" ]] || fail "$scenario: duplicate child PID"
  validate_child "$first"
  validate_child "$second"

  case $scenario in
  all-running)
    kill -TERM "$parent" || fail "$scenario: cannot signal parent"
    ;;
  part-finished)
    await_exit "$first"
    if ! running "$parent" || ! running "$second"; then
      fail "$scenario: second task or parent ended early"
    fi
    kill -TERM "$parent" || fail "$scenario: cannot signal parent"
    ;;
  esac
  await_exit "$parent"
  if wait "$parent"; then
    status=0
  else
    status=$?
  fi
  [[ $status == "$expected" ]] || fail "$scenario: expected status $expected, got $status"
  [[ ! -e /proc/$first && ! -e /proc/$second ]] || fail "$scenario: child still exists after parent exit"
  running "$sentinel" || fail "$scenario: unrelated process was terminated"
  elapsed=$((SECONDS - start))
  if [[ $scenario == normal && $elapsed -lt 3 ]]; then
    fail "$scenario: parent ended before the longer task's duration"
  fi
  kill -TERM "$sentinel"
  wait "$sentinel" 2>/dev/null || :
  printf 'PASS: %s\n' "$scenario"
}

if [[ ${1:-} == --inside ]]; then
  [[ $# == 1 && ${JADE_CLEANUP_TEST_INSIDE:-} == 1 && -f /.dockerenv ]] || fail 'internal runner requires the isolated container'
  [[ ${BASH_VERSION%%(*} == "${EXPECTED_BASH_VERSION:?missing runtime version}" ]] || fail 'unexpected Bash version'
  run_case normal 2 3 0
  run_case all-running 30 30 143
  run_case part-finished 1 30 143
  printf 'managed-child-cleanup tests passed\n'
else
  run_isolated "$@"
fi
