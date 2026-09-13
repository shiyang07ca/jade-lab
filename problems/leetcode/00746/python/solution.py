from __future__ import annotations

from functools import cache

# Created by shiyang07ca at 2023/12/17 19:09
# leetgo: dev
# https://leetcode.cn/problems/min-cost-climbing-stairs/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(cost):
                return 0
            return min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))

        return min(dfs(0), dfs(1))


# @lc code=end

if __name__ == "__main__":
    cost: list[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostClimbingStairs(cost)

    print("\noutput:", serialize(ans))
