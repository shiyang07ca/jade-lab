#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
readonly SCRIPT_DIR
TEMP_DIR=$(mktemp -d)
trap 'rm -rf -- "$TEMP_DIR"' EXIT

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

assert_contains() {
  local output=$1
  local expected=$2
  grep -Fq -- "$expected" <<<"$output" || fail "missing output: $expected"
}

assert_not_contains() {
  local output=$1
  local unexpected=$2
  if grep -Fq -- "$unexpected" <<<"$output"; then
    fail "unexpected output: $unexpected"
  fi
}

assert_status() {
  local expected=$1
  local description=$2
  shift 2
  local actual
  set +e
  "$@" >/dev/null 2>&1
  actual=$?
  set -e
  [[ $actual -eq $expected ]] ||
    fail "$description: expected status $expected, got $actual"
}

cat >"$TEMP_DIR/app.log" <<'LOG'
2026-08-10 08:00:01 [INFO] Server started
2026-08-10 08:01:00 [WARN] Pool nearly full
2026-08-10 08:02:00 [ERROR] Database unavailable
2026-08-10 08:03:00 [ERROR] Database unavailable
2026-08-10 08:04:00 [FATAL] Shutdown requested
LOG

output=$(bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --alert-threshold 99)
assert_contains "$output" "lines:  5"
assert_contains "$output" "ERROR:  2"
assert_contains "$output" "FATAL:  1"
assert_contains "$output" "2 Database unavailable"
assert_contains "$output" "ERROR density is higher in the second half"

help_output=$(bash "$SCRIPT_DIR/analyze-log.sh" --help)
assert_contains "$help_output" "Usage:"

cp "$TEMP_DIR/app.log" "$TEMP_DIR/log with spaces.log"
space_output=$(bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/log with spaces.log" --alert-threshold 000000099)
assert_contains "$space_output" "lines:  5"

leading_zero_output=$(bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --alert-threshold 000999999999)
assert_contains "$leading_zero_output" "lines:  5"

: >"$TEMP_DIR/empty.log"
empty_output=$(bash "$SCRIPT_DIR/analyze-log.sh" --alert-threshold 0 "$TEMP_DIR/empty.log" 2>&1)
assert_contains "$empty_output" "lines:  0"
assert_contains "$empty_output" "reached threshold 0"

cat >"$TEMP_DIR/many.log" <<'LOG'
2026-08-10 08:00:00 [ERROR] Message 1
2026-08-10 08:00:01 [ERROR] Message 2
2026-08-10 08:00:02 [ERROR] Message 3
2026-08-10 08:00:03 [ERROR] Message 4
2026-08-10 08:00:04 [ERROR] Message 5
2026-08-10 08:00:05 [ERROR] Message 6
2026-08-10 08:00:06 [ERROR] Message 7
LOG
many_output=$(bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/many.log" --alert-threshold 99)
assert_contains "$many_output" "ERROR:  7"
assert_contains "$many_output" "1 Message 5"
assert_not_contains "$many_output" "1 Message 6"
assert_not_contains "$many_output" "1 Message 7"

top_output=$(bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/many.log" --alert-threshold 99 --top 3)
assert_contains "$top_output" "1 Message 1"
assert_contains "$top_output" "1 Message 2"
assert_contains "$top_output" "1 Message 3"
assert_not_contains "$top_output" "1 Message 4"
assert_not_contains "$top_output" "1 Message 5"
assert_not_contains "$top_output" "1 Message 6"
assert_not_contains "$top_output" "1 Message 7"

assert_status 2 "missing log file" bash "$SCRIPT_DIR/analyze-log.sh"
assert_status 1 "unreadable path" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/missing.log"
assert_status 1 "invalid threshold" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --alert-threshold nope
assert_status 1 "oversized threshold" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --alert-threshold 1000000000
assert_status 1 "unknown option" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --unknown
assert_status 1 "extra positional argument" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" extra
assert_status 1 "missing webhook value" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --webhook
assert_status 1 "unsupported webhook scheme" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --webhook file:///tmp/alert
assert_status 1 "missing top value" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --top
assert_status 1 "zero top" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --top 0
assert_status 1 "negative top" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --top -1
assert_status 1 "oversized top" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --top 101
assert_status 1 "non-numeric top" bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --top nope

printf 'log-analyzer tests passed\n'
