from __future__ import annotations

# Created by shiyang07ca at 2024/05/03 22:34
# leetgo: dev
# https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def average(self, salary: list[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


# @lc code=end

if __name__ == "__main__":
    salary: list[int] = deserialize("List[int]", read_line())
    ans = Solution().average(salary)
    print("\noutput:", serialize(ans, "double"))
