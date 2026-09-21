from __future__ import annotations

# Created by shiyang07ca at 2023/08/24 00:09
# leetgo: dev
# https://leetcode.cn/problems/count-servers-that-communicate/
from typing import Counter

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rowc, colc = Counter(), Counter()
        for i, row in enumerate(grid):
            for j, g in enumerate(row):
                if g == 1:
                    rowc[i] += 1
                    colc[j] += 1

        ans = 0
        for i, row in enumerate(grid):
            for j, g in enumerate(row):
                if g == 1 and (rowc[i] > 1 or colc[j] > 1):
                    ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    grid: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countServers(grid)

    print("\noutput:", serialize(ans))
