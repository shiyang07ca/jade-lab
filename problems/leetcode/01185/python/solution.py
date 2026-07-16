# Created by shiyang07ca at 2023/12/30 00:07
# leetgo: dev
# https://leetcode.cn/problems/day-of-the-week/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/day-of-the-week/solutions/1187956/yi-zhou-zhong-de-di-ji-tian-by-leetcode-w43iw/链接：https://leetcode.cn/problems/day-of-the-week/solutions/1187956/yi-zhou-zhong-de-di-ji-tian-by-leetcode-w43iw/
    def dayOfTheWeek1(self, day: int, month: int, year: int) -> str:
        week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = 0
        # 输入年份之前的年份的天数贡献
        days += 365 * (year - 1971) + (year - 1969) // 4
        # 输入年份中，输入月份之前的月份的天数贡献
        days += sum(monthDays[: month - 1])
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month >= 3:
            days += 1
        # 输入月份中的天数贡献
        days += day

        return week[(days + 3) % 7]

    def dayOfTheWeek2(self, day: int, month: int, year: int) -> str:
        return [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][datetime.datetime(year, month, day).weekday()]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(year):
            return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

        ws = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ans = 3
        for i in range(1971, year):
            ans += 366 if is_leap(i) else 365
        for i in range(1, month):
            ans += ms[i - 1]
            if i == 2 and is_leap(year):
                ans += 1
        ans += day
        return ws[ans % 7]


# @lc code=end

if __name__ == "__main__":
    day: int = deserialize("int", read_line())
    month: int = deserialize("int", read_line())
    year: int = deserialize("int", read_line())
    ans = Solution().dayOfTheWeek(day, month, year)

    print("\noutput:", serialize(ans))
