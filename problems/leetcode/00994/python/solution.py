# Created by shiyang07ca at 2024/05/13 00:03
# leetgo: dev
# https://leetcode.cn/problems/rotting-oranges/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    q.append((i, j))

        t = 0
        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)
                for dx, dy in pairwise([-1, 0, 1, 0, -1]):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = 2
            if q:
                t += 1
        cnt1 = 0
        for row in grid:
            for x in row:
                if x == 1:
                    cnt1 += 1

        return t if cnt1 == 0 else -1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orangesRotting(grid)
    print("\noutput:", serialize(ans, "integer"))
