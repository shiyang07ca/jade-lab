# Created by shiyang07ca at 2024/05/31 23:38
# leetgo: dev
# https://leetcode.cn/problems/find-missing-and-repeated-values/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = Counter()
        for row in grid:
            for x in row:
                cnt[x] += 1
        a = b = 0
        for i in range(1, n * n + 1):
            if cnt[i] == 2:
                a = i
            if cnt[i] == 0:
                b = i
        return [a, b]


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMissingAndRepeatedValues(grid)
    print("\noutput:", serialize(ans, "integer[]"))
