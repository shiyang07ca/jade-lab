from __future__ import annotations

# Created by shiyang07ca at 2023/08/07 00:03
# leetgo: dev
# https://leetcode.cn/problems/reverse-string/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


# @lc code=end

if __name__ == "__main__":
    s: list[str] = deserialize("List[str]", read_line())
    Solution().reverseString(s)
    ans = s

    print("\noutput:", serialize(ans))
