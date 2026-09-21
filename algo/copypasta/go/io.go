package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// run keeps input and output injectable for local OJ tests.
func run(reader io.Reader, writer io.Writer) {
	in := bufio.NewReader(reader)
	out := bufio.NewWriter(writer)
	defer out.Flush()

	var left, right int
	if _, err := fmt.Fscan(in, &left, &right); err != nil {
		return
	}
	fmt.Fprintln(out, left+right)
}

func main() {
	run(os.Stdin, os.Stdout)
}
