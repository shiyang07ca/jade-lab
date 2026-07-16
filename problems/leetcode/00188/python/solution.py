# Created by shiyang07ca at 2023/10/04 20:48
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/2201488/shi-pin-jiao-ni-yi-bu-bu-si-kao-dong-tai-kksg/
    # 记忆化
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, hold: bool) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, k, False)

    # 递推
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            f[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + p)
                f[i + 1][j][1] = max(f[i][j][1], f[i][j - 1][0] - p)
        return f[n][k + 1][0]


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(k, prices)

    print("\noutput:", serialize(ans))
