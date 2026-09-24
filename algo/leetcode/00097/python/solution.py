# Created by shiyang07ca at 2026/09/22 23:12
# leetgo: 1.4.17
# https://leetcode.cn/problems/interleaving-string/

from functools import cache
from typing import *

from leetgo_py import *

# @lc code=begin


# TODO
# 链接：https://leetcode.cn/problems/interleaving-string/solutions/3060419/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-qcen/
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        @cache
        def dfs(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            return (
                (
                    i >= 0
                    and s1[i] == s3[i + j + 1]
                    and dfs(i - 1, j)
                )
                or (
                    j >= 0
                    and s2[j] == s3[i + j + 1]
                    and dfs(i, j - 1)
                )
            )

        return dfs(n - 1, m - 1)


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    s3: str = deserialize("str", read_line())
    ans = Solution().isInterleave(s1, s2, s3)
    print("\noutput:", serialize(ans, "boolean"))
