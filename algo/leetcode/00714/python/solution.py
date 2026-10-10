from __future__ import annotations

from functools import cache
from math import inf

# Created by shiyang07ca at 2023/10/06 00:14
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash = 0  # 今天结束时，不持有股票的最大累计净收益
        hold = -prices[0]  # 今天结束时，持有股票的最大累计净收益

        for i in range(1, len(prices)):
            price = prices[i]

            # 两个新状态都使用昨天的状态计算。
            new_cash = max(cash, hold + price - fee)
            new_hold = max(hold, cash - price)

            cash = new_cash
            hold = new_hold

        return cash


class Solution2:
    def maxProfit(self, prices: list[int], fee: int) -> int:

        @cache
        def dfs(i: int, hold: bool) -> int | float:
            # 第 i 天结束时，处于指定持股状态的最大净收益。
            if i < 0:
                # 交易开始前不可能持股，用负无穷排除该状态。
                return -inf if hold else 0

            if hold:
                return max(
                    dfs(i - 1, True),  # 继续持有。
                    dfs(i - 1, False) - prices[i],  # 今天买入。
                )

            return max(
                dfs(i - 1, False),  # 继续不持股。
                dfs(i - 1, True) + prices[i] - fee,  # 今天卖出。
            )

        # 不持股状态至少可以选择不交易，最终结果一定是有限整数。
        return int(dfs(len(prices) - 1, False))


# @lc code=end

if __name__ == "__main__":
    prices: list[int] = deserialize("List[int]", read_line())
    fee: int = deserialize("int", read_line())
    ans = Solution().maxProfit(prices, fee)

    print("\noutput:", serialize(ans))
