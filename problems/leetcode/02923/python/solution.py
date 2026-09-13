from __future__ import annotations

# Created by shiyang07ca at 2024/04/13 15:30
# leetgo: dev
# https://leetcode.cn/problems/find-champion-i/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for row in grid:
            if row.count(0) == 1:
                return row.index(0)
        raise ValueError("no champion")


# @lc code=end

if __name__ == "__main__":
    grid: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findChampion(grid)
    print("\noutput:", serialize(ans, "integer"))
