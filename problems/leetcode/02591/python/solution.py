# Created by shiyang07ca at 2023/09/22 13:36
# leetgo: dev
# https://leetcode.cn/problems/distribute-money-to-maximum-children/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1

        def check(x):
            return (
                x * 8 <= money
                and (money - x * 8) >= (children - x)
                and not ((money - x * 8) > 0 and children == x)
                and not ((money - x * 8) == 4 and children - x == 1)
            )

        l, r = 0, children
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return r


# @lc code=end

if __name__ == "__main__":
    money: int = deserialize("int", read_line())
    children: int = deserialize("int", read_line())
    ans = Solution().distMoney(money, children)

    print("\noutput:", serialize(ans))
