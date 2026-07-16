# Created by shiyang07ca at 2023/12/29 00:06
# leetgo: dev
# https://leetcode.cn/problems/buy-two-chocolates/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s = prices[0] + prices[1]
        if s <= money:
            return money - s
        else:
            return money


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    money: int = deserialize("int", read_line())
    ans = Solution().buyChoco(prices, money)

    print("\noutput:", serialize(ans))
