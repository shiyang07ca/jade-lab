# Created by shiyang07ca at 2023/05/03 22:33
# https://leetcode.cn/problems/coin-change/

"""
322. 零钱兑换 (Medium)
给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数
`amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有
任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

**示例 1：**

```
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0

```

**提示：**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2³¹ - 1`
- `0 <= amount <= 10⁴`

"""
from functools import *
from math import *
from typing import *
from leetgo_py import *

# @lc code=begin

# template
# tag: dp, knapsack


class Solution:
    # 记忆化搜索
    def coinChange1(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        n = len(coins)
        ans = dfs(n - 1, amount)
        return ans if ans is not inf else -1

    # 递推
    def coinChange2(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)

        ans = f[n][amount]
        return ans if ans is not inf else -1

    # 滚动数组
    def coinChange3(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [inf] * (amount + 1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)

        ans = f[amount]
        return ans if ans is not inf else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for v in coins:
            # 完全背包模版
            # dp[i] 表示兑换 i 金额的最小硬币数
            for i in range(v, amount + 1):
                if dp[i - v] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - v] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - v] + 1)

        return dp[amount]


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("output:", serialize(ans))
