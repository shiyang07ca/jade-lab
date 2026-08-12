package main

import "testing"

func TestRequireNonNegative(t *testing.T) {
	if got := requireNonNegative(0); got != 0 {
		t.Fatalf("requireNonNegative(0) = %d, want 0", got)
	}
}

func TestRequireNonNegativePanics(t *testing.T) {
	defer func() {
		if recovered := recover(); recovered == nil {
			t.Fatal("requireNonNegative(-1) did not panic")
		}
	}()

	requireNonNegative(-1)
}
