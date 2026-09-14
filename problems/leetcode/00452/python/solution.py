# Created by shiyang07ca at 2026/09/14 23:50
# leetgo: 1.4.17
# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

from sys import maxsize as inf
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = 0
        pre_end = -inf
        for start, end in points:
            if start > pre_end:
                pre_end = end
                res += 1
            else:
                pre_end = min(pre_end, end)

        return res


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinArrowShots(points)
    print("\noutput:", serialize(ans, "integer"))
