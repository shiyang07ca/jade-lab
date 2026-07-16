# Created by shiyang07ca at 2023/08/10 10:04
# leetgo: dev
# https://leetcode.cn/problems/minimum-falling-path-sum-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minFallingPathSum1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cur = grid[0][:]
        pre = grid[0][:]
        for row in grid[1:]:
            for i in range(n):
                cur[i] = row[i] + min(*pre[:i], *pre[i + 1 :])
            pre = cur[:]
        return min(cur)

    # 链接：https://leetcode.cn/problems/minimum-falling-path-sum-ii/solutions/2381174/python3javacgotypescript-yi-ti-yi-jie-do-sko0/
    def minFallingPathSum2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[0] * n for _ in range(n + 1)]
        for i, row in enumerate(grid, 1):
            for j, v in enumerate(row):
                x = min((f[i - 1][k] for k in range(n) if k != j), default=0)
                f[i][j] = v + x
        return min(f[n])


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(grid)

    print("\noutput:", serialize(ans))
