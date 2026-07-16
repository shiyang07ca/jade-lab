# Created by shiyang07ca at 2023/10/05 21:00
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 记忆化
    def maxProfit(self, prices: List[int]) -> int:
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
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
