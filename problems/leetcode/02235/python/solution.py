from __future__ import annotations

# Created by shiyang07ca at 2023/08/19 22:22
# leetgo: dev
# https://leetcode.cn/problems/add-two-integers/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# @lc code=end

if __name__ == "__main__":
    num1: int = deserialize("int", read_line())
    num2: int = deserialize("int", read_line())
    ans = Solution().sum(num1, num2)

    print("\noutput:", serialize(ans))
