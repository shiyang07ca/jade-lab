# Created by shiyang07ca at 2023/11/08 13:45
# leetgo: dev
# https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            c0 = c1 = 0
            for j in range(i, n):
                if s[j] == "0":
                    c0 += 1
                    if c1 > 0:
                        break
                if s[j] == "1":
                    c1 += 1

                if c1 > c0:
                    break
                if c0 == c1:
                    ans = max(ans, j - i + 1)
                    break

        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findTheLongestBalancedSubstring(s)

    print("\noutput:", serialize(ans))
