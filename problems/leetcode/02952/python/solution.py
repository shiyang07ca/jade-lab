# Created by shiyang07ca at 2024/03/30 00:07
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Greedy


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/solutions/2551707/yong-gui-na-fa-si-kao-pythonjavacgo-by-e-8etj/
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans, s, i = 0, 1, 0
        while s <= target:
            if i < len(coins) and coins[i] <= s:
                s += coins[i]
                i += 1
            else:
                s *= 2  # 必须添加 s
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimumAddedCoins(coins, target)

    print("\noutput:", serialize(ans))
