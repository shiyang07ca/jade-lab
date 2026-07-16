# Created by shiyang07ca at 2024/04/27 10:08
# leetgo: dev
# https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for j in range(len(grid[0])):
            t = 0
            for i in range(len(grid)):
                t = max(t, len(str(grid[i][j])))
            ans.append(t)
        return ans


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findColumnWidth(grid)
    print("\noutput:", serialize(ans, "integer[]"))
