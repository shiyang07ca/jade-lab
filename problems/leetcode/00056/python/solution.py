# Created by shiyang07ca at 2023/08/27 12:19
# leetgo: dev
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for a, b in intervals[1:]:
            if a <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], b)]
            else:
                ans.append([a, b])
        return ans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)

    print("\noutput:", serialize(ans))
