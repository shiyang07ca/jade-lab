package main

import "fmt"

// DisjointSet maintains components for elements in [0, size).
type DisjointSet struct {
	parent     []int
	components []int
	count      int
}

func NewDisjointSet(size int) *DisjointSet {
	if size < 0 {
		panic("size must be non-negative")
	}
	parent := make([]int, size)
	components := make([]int, size)
	for index := range size {
		parent[index] = index
		components[index] = 1
	}
	return &DisjointSet{parent: parent, components: components, count: size}
}

func (set *DisjointSet) validate(element int) {
	if element < 0 || element >= len(set.parent) {
		panic(fmt.Sprintf("element %d is outside the disjoint set", element))
	}
}

func (set *DisjointSet) Find(element int) int {
	set.validate(element)
	root := element
	for root != set.parent[root] {
		root = set.parent[root]
	}
	for element != root {
		parent := set.parent[element]
		set.parent[element] = root
		element = parent
	}
	return root
}

func (set *DisjointSet) Union(left, right int) bool {
	leftRoot := set.Find(left)
	rightRoot := set.Find(right)
	if leftRoot == rightRoot {
		return false
	}
	if set.components[leftRoot] < set.components[rightRoot] {
		leftRoot, rightRoot = rightRoot, leftRoot
	}
	set.parent[rightRoot] = leftRoot
	set.components[leftRoot] += set.components[rightRoot]
	set.count--
	return true
}

func (set *DisjointSet) Connected(left, right int) bool {
	return set.Find(left) == set.Find(right)
}

func (set *DisjointSet) ComponentSize(element int) int {
	return set.components[set.Find(element)]
}

func (set *DisjointSet) ComponentCount() int {
	return set.count
}
