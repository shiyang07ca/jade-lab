# Created by shiyang07ca at 2024/04/25 00:01
# leetgo: dev
# https://leetcode.cn/problems/total-distance-traveled/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            mainTank -= 5
            ans += 50
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
        return ans + mainTank * 10


# @lc code=end

if __name__ == "__main__":
    mainTank: int = deserialize("int", read_line())
    additionalTank: int = deserialize("int", read_line())
    ans = Solution().distanceTraveled(mainTank, additionalTank)
    print("\noutput:", serialize(ans, "integer"))
