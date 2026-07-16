# Created by shiyang07ca at 2023/07/18 09:25
# leetgo: dev
# https://leetcode.cn/problems/minimum-interval-to-include-each-query/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: heap


# 链接：https://leetcode.cn/problems/minimum-interval-to-include-each-query/solutions/2348342/python3javacgo-yi-ti-yi-jie-pai-xu-chi-x-5mgt/
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        queries = sorted((x, i) for i, x in enumerate(queries))
        ans = [-1] * m
        pq = []
        i = 0
        for x, j in queries:
            while i < n and intervals[i][0] <= x:
                a, b = intervals[i]
                heappush(pq, (b - a + 1, b))
                i += 1
            while pq and pq[0][1] < x:
                heappop(pq)
            if pq:
                ans[j] = pq[0][0]
        return ans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minInterval(intervals, queries)

    print("\noutput:", serialize(ans))
