# Created by shiyang07ca at 2026/09/28 21:17
# leetgo: 1.4.17
# https://leetcode.cn/problems/non-overlapping-intervals/

from math import inf
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO

# 链接：https://leetcode.cn/problems/non-overlapping-intervals/solutions/3077218/tan-xin-zheng-ming-pythonjavaccgojsrust-3jx4f/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        pre_r = -inf
        for start, end in intervals:
            if start >= pre_r:
                ans += 1
                pre_r = end
        return len(intervals) - ans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eraseOverlapIntervals(intervals)
    print("\noutput:", serialize(ans, "integer"))
