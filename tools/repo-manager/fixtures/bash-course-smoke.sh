#!/usr/bin/env bash

set -uo pipefail

die() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

assert_equal() {
  local expected=$1
  local actual=$2
  local label=$3
  [[ $actual == "$expected" ]] || die "$label: expected '$expected', got '$actual'"
}

test_runtime() {
  local actual=${BASH_VERSION%%(*}
  assert_equal "${EXPECTED_BASH_VERSION:?missing EXPECTED_BASH_VERSION}" "$actual" "Bash version"
}

test_quoted_arguments() {
  local values=("alpha" "two words" "*.txt")
  local count
  count=$(printf '%s\n' "${values[@]}" | wc -l | tr -d ' ')
  assert_equal "3" "$count" 'quoted argument count'
}

test_pipefail() {
  if (
    set -o pipefail
    false | true
  ); then
    die 'pipefail did not preserve an upstream failure'
  fi
}

test_errexit_context() {
  local output
  output=$(bash -c 'set -e; if false; then :; fi; printf survived')
  assert_equal "survived" "$output" 'errexit condition context'
}

test_wait_statuses() {
  local first_pid second_pid first_status=0 second_status=0
  (sh -c 'exit 7') &
  first_pid=$!
  (sh -c 'exit 0') &
  second_pid=$!
  wait "$first_pid" || first_status=$?
  wait "$second_pid" || second_status=$?
  assert_equal "7" "$first_status" 'first child status'
  assert_equal "0" "$second_status" 'second child status'
}

test_exit_cleanup() {
  local directory marker
  directory=$(mktemp -d)
  marker=$directory/cleaned
  MARKER=$marker bash -c 'trap '\''printf cleaned >"$MARKER"'\'' EXIT; exit 3' || :
  assert_equal "cleaned" "$(<"$marker")" 'EXIT cleanup'
  find "$directory" -depth -delete
}

main() {
  test_runtime
  test_quoted_arguments
  test_pipefail
  test_errexit_context
  test_wait_statuses
  test_exit_cleanup
  printf 'Bash course smoke checks passed\n'
}

main "$@"
