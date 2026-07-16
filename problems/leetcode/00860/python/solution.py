# Created by shiyang07ca at 2023/07/22 18:04
# leetgo: dev
# https://leetcode.cn/problems/lemonade-change/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x = y = 0
        for b in bills:
            if b == 5:
                x += 1
            elif b == 10:
                if x == 0:
                    return False
                y += 1
                x -= 1
            else:
                if y >= 1 and x >= 1:
                    x -= 1
                    y -= 1
                elif x >= 3:
                    x -= 3
                else:
                    return False

        return True


# @lc code=end

if __name__ == "__main__":
    bills: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lemonadeChange(bills)

    print("\noutput:", serialize(ans))
