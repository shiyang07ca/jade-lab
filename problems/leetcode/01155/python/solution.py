# Created by shiyang07ca at 2023/10/24 13:26
# leetgo: dev
# https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(n, target):
            if target < 0 or (target > 0 and n == 0):
                return 0
            if n == 0 and target == 0:
                return 1

            ans = 0
            for i in range(1, min(k, target) + 1):
                ans = (ans + dfs(n - 1, target - i)) % MOD
            return ans

        return dfs(n, target)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numRollsToTarget(n, k, target)

    print("\noutput:", serialize(ans))
