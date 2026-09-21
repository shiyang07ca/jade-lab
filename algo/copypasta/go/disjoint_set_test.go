package main

import "testing"

func TestDisjointSet(t *testing.T) {
	set := NewDisjointSet(6)
	if !set.Union(0, 1) || !set.Union(1, 2) {
		t.Fatal("expected distinct components to merge")
	}
	if set.Union(0, 2) {
		t.Fatal("expected repeated union to report no merge")
	}
	if !set.Connected(0, 2) || set.Connected(0, 3) {
		t.Fatal("unexpected connectivity result")
	}
	if size := set.ComponentSize(1); size != 3 {
		t.Fatalf("ComponentSize(1) = %d, want 3", size)
	}
	if count := set.ComponentCount(); count != 4 {
		t.Fatalf("ComponentCount() = %d, want 4", count)
	}
}

func TestDisjointSetRejectsInvalidElement(t *testing.T) {
	defer func() {
		if recover() == nil {
			t.Fatal("Find should panic for an invalid element")
		}
	}()
	NewDisjointSet(2).Find(2)
}

func TestDisjointSetRejectsNegativeSize(t *testing.T) {
	defer func() {
		if recover() == nil {
			t.Fatal("NewDisjointSet should panic for a negative size")
		}
	}()
	NewDisjointSet(-1)
}
