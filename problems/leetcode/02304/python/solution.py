# Created by shiyang07ca at 2023/11/22 13:05
# leetgo: dev
# https://leetcode.cn/problems/minimum-path-cost-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j):
            if i == 0:
                return grid[0][j]
            ans = inf
            for k in range(n):
                ans = min(ans, dfs(i - 1, k) + moveCost[grid[i - 1][k]][j] + grid[i][j])
            return ans

        return min(dfs(m - 1, j) for j in range(n))


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    moveCost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathCost(grid, moveCost)

    print("\noutput:", serialize(ans))
