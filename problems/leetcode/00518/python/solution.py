# Created by shiyang07ca at 2024/03/25 21:54
# leetgo: dev
# https://leetcode.cn/problems/coin-change-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, n):
            if i >= len(coins):
                return 1 if n == 0 else 0

            if n < coins[i]:
                return dfs(i + 1, n)

            return dfs(i + 1, n) + dfs(i, n - coins[i])

        coins.sort(reverse=True)
        return dfs(0, amount)


# @lc code=end

if __name__ == "__main__":
    amount: int = deserialize("int", read_line())
    coins: List[int] = deserialize("List[int]", read_line())
    ans = Solution().change(amount, coins)

    print("\noutput:", serialize(ans))
