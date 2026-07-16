# Created by shiyang07ca at 2024/04/13 15:30
# leetgo: dev
# https://leetcode.cn/problems/find-champion-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for row in grid:
            if row.count(0) == 1:
                return row.index(0)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findChampion(grid)
    print("\noutput:", serialize(ans, "integer"))
