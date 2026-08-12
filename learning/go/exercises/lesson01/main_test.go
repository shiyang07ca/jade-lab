package main

import (
	"reflect"
	"testing"
)

func TestCountWords(t *testing.T) {
	t.Parallel()

	got := countWords("go  go\npython")
	want := map[string]int{"go": 2, "python": 1}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("countWords() = %v, want %v", got, want)
	}
}

func TestCountWordsEmpty(t *testing.T) {
	t.Parallel()

	got := countWords(" \t\n")
	if len(got) != 0 {
		t.Fatalf("countWords() = %v, want empty map", got)
	}
}
