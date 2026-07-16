# Created by shiyang07ca at 2023/10/02 00:01
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        pre = prices[0]
        ans = 0
        for p in prices:
            if p > pre:
                ans += p - pre
            pre = p
        return ans

    # 递归 + 记忆化
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, hold), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, hold), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)

    # 递推
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf
        for i, p in enumerate(prices):
            f[i + 1][0] = max(f[i][0], f[i][1] + p)
            f[i + 1][1] = max(f[i][1], f[i][0] - p)

        return f[n][0]


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
