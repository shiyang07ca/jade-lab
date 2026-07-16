# Created by shiyang07ca at 2023/12/10 19:22
# leetgo: dev
# https://leetcode.cn/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 1 or n == 2:
                return n
            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)

    print("\noutput:", serialize(ans))
