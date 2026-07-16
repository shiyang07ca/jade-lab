# Created by shiyang07ca at 2024/05/10 21:55
# leetgo: dev
# https://leetcode.cn/problems/count-tested-devices-after-test-operations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countTestedDevices(self, ps: List[int]) -> int:
        ans = 0
        n = len(ps)
        for i, p in enumerate(ps):
            if p > 0:
                ans += 1
                for j in range(i + 1, n):
                    ps[j] = max(0, ps[j] - 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    batteryPercentages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTestedDevices(batteryPercentages)
    print("\noutput:", serialize(ans, "integer"))
