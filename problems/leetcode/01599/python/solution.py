# Created by shiyang07ca at 2024/01/01 00:48
# leetgo: dev
# https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Simulation


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/solutions/2586522/python3javacgorust-yi-ti-yi-jie-mo-ni-qi-zstw/
    def minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int
    ) -> int:
        ans = -1
        mx = t = 0
        wait = 0
        i = 0
        while wait or i < len(customers):
            wait += customers[i] if i < len(customers) else 0
            up = wait if wait < 4 else 4
            wait -= up
            t += up * boardingCost - runningCost
            i += 1
            if t > mx:
                mx = t
                ans = i
        return ans


# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    boardingCost: int = deserialize("int", read_line())
    runningCost: int = deserialize("int", read_line())
    ans = Solution().minOperationsMaxProfit(customers, boardingCost, runningCost)

    print("\noutput:", serialize(ans))
