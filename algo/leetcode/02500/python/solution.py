from __future__ import annotations

# Created by shiyang07ca at 2023/07/27 09:29
# leetgo: dev
# https://leetcode.cn/problems/delete-greatest-value-in-each-row/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        ans = 0
        for col in zip(*grid):
            ans += max(col)
        return ans


# @lc code=end

if __name__ == "__main__":
    grid: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().deleteGreatestValue(grid)

    print("\noutput:", serialize(ans))
