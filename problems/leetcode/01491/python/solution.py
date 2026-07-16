# Created by shiyang07ca at 2024/05/03 22:34
# leetgo: dev
# https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


# @lc code=end

if __name__ == "__main__":
    salary: List[int] = deserialize("List[int]", read_line())
    ans = Solution().average(salary)
    print("\noutput:", serialize(ans, "double"))
