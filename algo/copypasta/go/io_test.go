package main

import (
	"bytes"
	"strings"
	"testing"
)

func TestRunAddsTwoIntegers(t *testing.T) {
	var output bytes.Buffer
	run(strings.NewReader("19 23\n"), &output)
	if got, want := output.String(), "42\n"; got != want {
		t.Fatalf("run output = %q, want %q", got, want)
	}
}

func TestRunIgnoresIncompleteInput(t *testing.T) {
	var output bytes.Buffer
	run(strings.NewReader("19\n"), &output)
	if got := output.String(); got != "" {
		t.Fatalf("run output = %q, want empty output", got)
	}
}
