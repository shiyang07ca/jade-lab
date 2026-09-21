package main

import (
	"fmt"
	"strings"
)

func countWords(text string) map[string]int {
	counts := make(map[string]int)
	for _, word := range strings.Fields(text) {
		counts[word]++
	}
	return counts
}

func main() {
	fmt.Println(countWords("go go go python go"))
}
