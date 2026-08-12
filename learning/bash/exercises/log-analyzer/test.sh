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

if bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --alert-threshold nope >/dev/null 2>&1; then
  fail "invalid threshold was accepted"
fi

if bash "$SCRIPT_DIR/analyze-log.sh" "$TEMP_DIR/app.log" --webhook >/dev/null 2>&1; then
  fail "missing option value was accepted"
fi

printf 'log-analyzer tests passed\n'
