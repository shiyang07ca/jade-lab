# Created by shiyang07ca at 2023/08/07 00:03
# leetgo: dev
# https://leetcode.cn/problems/reverse-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseString(self, s: List[str]) -> None:
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
    s: List[str] = deserialize("List[str]", read_line())
    reverseString(s)
    ans = s

    print("\noutput:", serialize(ans))
