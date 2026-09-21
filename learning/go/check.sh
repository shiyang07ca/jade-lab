#!/bin/sh

set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

export GOTOOLCHAIN=local
expected_go=go1.26.5
if command -v go >/dev/null 2>&1; then
  actual_go=$(go env GOVERSION)
else
  actual_go=missing
fi
if [ "$actual_go" != "$expected_go" ] && command -v mise >/dev/null 2>&1; then
  exec mise exec -- sh "$script_dir/check.sh"
fi
if [ "$actual_go" != "$expected_go" ]; then
  printf 'expected %s, got %s\n' "$expected_go" "$actual_go" >&2
  exit 1
fi

unformatted=$(gofmt -l exercises)
if [ -n "$unformatted" ]; then
  printf 'gofmt required:\n%s\n' "$unformatted" >&2
  exit 1
fi

cd exercises
go mod tidy -diff
go vet ./...
go test -count=1 ./...
go test -race -count=1 ./...

build_dir=$(mktemp -d "${TMPDIR:-/tmp}/jade-go-course.XXXXXX")
trap 'rm -rf -- "$build_dir"' 0 HUP INT TERM
go build -o "$build_dir/" ./...
