// Created by shiyang07ca at 2026/10/02 14:42
// leetgo: 1.4.17
// https://leetcode.cn/problems/string-compression/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

// 双指针：read 扫过一组连续相同字符，write 把「字符 + 组长度」写回原数组。
// 安全性来自 1 + 位数(run) <= run（run >= 2，且 run = 2 时取等号），
// 因此每一组结束时 write <= read，写指针只会覆盖自己刚读过的那一段。
func compress(chars []byte) int {
	n := len(chars)
	read, write := 0, 0
	for read < n {
		ch := chars[read]
		run := 0
		for read < n && chars[read] == ch {
			read++
			run++
		}
		chars[write] = ch
		write++
		if run > 1 {
			// run <= 2000，十进制最多 4 位，固定数组即可，不做任何分配。
			var buf [4]byte
			i := len(buf)
			for run > 0 {
				i--
				buf[i] = byte('0' + run%10)
				run /= 10
			}
			write += copy(chars[write:], buf[i:])
		}
	}
	return write
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	chars := Deserialize[[]byte](ReadLine(stdin))
	ans := compress(chars)

	fmt.Println("\noutput:", Serialize(ans))
}
