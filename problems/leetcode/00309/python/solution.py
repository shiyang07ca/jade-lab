from __future__ import annotations

from functools import cache
from sys import maxsize as inf

# Created by shiyang07ca at 2023/10/05 21:00
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # 记忆化
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)


# @lc code=end

if __name__ == "__main__":
    prices: list[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
