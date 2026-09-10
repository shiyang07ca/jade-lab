// Created by shiyang07ca at 2026/09/11 02:17
// leetgo: 1.4.17
// https://leetcode.cn/problems/merge-sorted-array/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func merge(nums1 []int, m int, nums2 []int, n int) {
	p1, p2, c := m-1, n-1, m+n-1
	for p2 >= 0 {
		if p1 >= 0 && nums1[p1] > nums2[p2] {
			nums1[c] = nums1[p1]
			p1--
		} else {
			nums1[c] = nums2[p2]
			p2--
		}
		c--
	}
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums1 := Deserialize[[]int](ReadLine(stdin))
	m := Deserialize[int](ReadLine(stdin))
	nums2 := Deserialize[[]int](ReadLine(stdin))
	n := Deserialize[int](ReadLine(stdin))
	merge(nums1, m, nums2, n)
	ans := nums1

	fmt.Println("\noutput:", Serialize(ans))
}
