# Created by shiyang07ca at 2023/09/01 13:16
# leetgo: dev
# https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        for i in range(total // cost1 + 1):
            ans += (total - i * cost1) // cost2 + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    total: int = deserialize("int", read_line())
    cost1: int = deserialize("int", read_line())
    cost2: int = deserialize("int", read_line())
    ans = Solution().waysToBuyPensPencils(total, cost1, cost2)

    print("\noutput:", serialize(ans))
