# Created by shiyang07ca at 2023/10/06 00:14
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import *
from math import *
from functools import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, hold), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, hold), dfs(i - 1, True) + prices[i] - fee)

        return dfs(n - 1, False)


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    fee: int = deserialize("int", read_line())
    ans = Solution().maxProfit(prices, fee)

    print("\noutput:", serialize(ans))
