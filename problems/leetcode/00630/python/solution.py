# Created by shiyang07ca at 2023/09/11 13:36
# leetgo: dev
# https://leetcode.cn/problems/course-schedule-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: greedy


class Solution:
    # 链接：https://leetcode.cn/problems/course-schedule-iii/solutions/2436667/tan-xin-huan-neng-fan-hui-pythonjavacgoj-lcwp/
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])  # 按照 last_day 从小到大排序
        h = []
        day = 0  # 已消耗时间
        for duration, last_day in courses:
            if day + duration <= last_day:  # 没有超过 last_day，直接学习
                day += duration
                heappush(h, -duration)  # 加负号变成最大堆
            elif h and duration < -h[0]:  # 该课程的时间比之前的最长时间要短
                # 反悔，撤销之前 duration 最长的课程，改为学习该课程
                # 节省出来的时间，能在后面上完更多的课程
                day -= -heapreplace(h, -duration) - duration
        return len(h)


# @lc code=end

if __name__ == "__main__":
    courses: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().scheduleCourse(courses)

    print("\noutput:", serialize(ans))
