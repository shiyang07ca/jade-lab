# Created by shiyang07ca at 2023/10/01 00:00
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = prices[-1]
        ans = 0
        for p in prices[::-1]:
            if p > max_p:
                max_p = p

            if (max_p - p) > ans:
                ans = max_p - p

        return ans


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
