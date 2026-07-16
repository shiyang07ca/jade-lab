# Created by shiyang07ca at 2023/12/31 00:10
# leetgo: dev
# https://leetcode.cn/problems/day-of-the-year/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def dayOfYear(self, date: str) -> int:
        def is_leap(year):
            return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

        ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split("-"))
        ans = d
        if is_leap(y) and m > 2:
            ans += 1
        ans += sum(ms[: m - 1])
        return ans


# @lc code=end

if __name__ == "__main__":
    date: str = deserialize("str", read_line())
    ans = Solution().dayOfYear(date)

    print("\noutput:", serialize(ans))
