package main

import "fmt"

// requireNonNegative guards an internal invariant. Expected user or I/O errors
// should normally be returned to the caller instead of converted to a panic.
func requireNonNegative(value int) int {
	if value < 0 {
		panic("value must be non-negative")
	}
	return value
}

func main() {
	fmt.Println(requireNonNegative(1))
}
