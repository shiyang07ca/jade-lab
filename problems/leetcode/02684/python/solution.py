# Created by shiyang07ca at 2023/11/08 18:46
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/

from functools import *
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxMoves(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])

        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            c = g[i][j]
            ans = 0
            if j + 1 < n and i >= 1 and c < g[i - 1][j + 1]:
                ans = max(ans, dfs(i - 1, j + 1) + 1)
            if j + 1 < n and i + 1 < m and c < g[i + 1][j + 1]:
                ans = max(ans, dfs(i + 1, j + 1) + 1)
            if j + 1 < n and c < g[i][j + 1]:
                ans = max(ans, dfs(i, j + 1) + 1)
            return ans

        return max(dfs(i, 0) for i in range(m))


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxMoves(grid)

    print("\noutput:", serialize(ans))
