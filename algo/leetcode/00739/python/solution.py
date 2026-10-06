# Created by shiyang07ca at 2026/10/07 02:10
# leetgo: 1.4.17
# https://leetcode.cn/problems/daily-temperatures/

from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []  # 尚未遇到更高温度的日期下标

        for today, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_day = stack.pop()
                answer[previous_day] = today - previous_day

            stack.append(today)

        return answer


# @lc code=end

if __name__ == "__main__":
    temperatures: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dailyTemperatures(temperatures)
    print("\noutput:", serialize(ans, "integer[]"))
