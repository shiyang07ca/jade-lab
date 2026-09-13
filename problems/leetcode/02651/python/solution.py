from __future__ import annotations

# Created by shiyang07ca at 2023/09/08 09:56
# leetgo: dev
# https://leetcode.cn/problems/calculate-delayed-arrival-time/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


# @lc code=end

if __name__ == "__main__":
    arrivalTime: int = deserialize("int", read_line())
    delayedTime: int = deserialize("int", read_line())
    ans = Solution().findDelayedArrivalTime(arrivalTime, delayedTime)

    print("\noutput:", serialize(ans))
