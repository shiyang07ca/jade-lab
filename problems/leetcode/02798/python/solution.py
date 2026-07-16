# Created by shiyang07ca at 2024/04/30 00:18
# leetgo: dev
# https://leetcode.cn/problems/number-of-employees-who-met-the-target/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([1 if h >= target else 0 for h in hours])


# @lc code=end

if __name__ == "__main__":
    hours: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numberOfEmployeesWhoMetTarget(hours, target)
    print("\noutput:", serialize(ans, "integer"))
