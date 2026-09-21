from __future__ import annotations

# Created by shiyang07ca at 2023/09/13 13:06
# leetgo: dev
# https://leetcode.cn/problems/check-knight-tour-configuration/
from itertools import pairwise

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        if grid[0][0] != 0:
            return False

        n = len(grid)
        pos: list[tuple[int, int]] = [(0, 0)] * (n * n)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pos[x] = (i, j)
        for (x1, y1), (x2, y2) in pairwise(pos):
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            if not (dx == 2 and dy == 1) and not (dx == 1 and dy == 2):
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    grid: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValidGrid(grid)

    print("\noutput:", serialize(ans))
