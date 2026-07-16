# Created by shiyang07ca at 2024/05/15 00:10
# leetgo: dev
# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/solutions/2163130/tan-xin-pythonjavacgo-by-endlesscheng-w3k3/
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        run = [False] * (tasks[-1][1] + 1)
        for start, end, d in tasks:
            d -= sum(run[start : end + 1])  # 去掉运行中的时间点
            if d <= 0:  # 该任务已完成
                continue
            # 该任务尚未完成，从后往前找没有运行的时间点
            for i in range(end, start - 1, -1):
                if run[i]:  # 已运行
                    continue
                run[i] = True  # 运行
                d -= 1
                if d == 0:
                    break
        return sum(run)


# @lc code=end

if __name__ == "__main__":
    tasks: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinimumTime(tasks)
    print("\noutput:", serialize(ans, "integer"))
