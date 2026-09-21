from __future__ import annotations

from heapq import heappop, heappush

# Created by shiyang07ca at 2023/07/18 09:25
# leetgo: dev
# https://leetcode.cn/problems/minimum-interval-to-include-each-query/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO
# tag: heap


# 链接：https://leetcode.cn/problems/minimum-interval-to-include-each-query/solutions/2348342/python3javacgo-yi-ti-yi-jie-pai-xu-chi-x-5mgt/
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        sorted_queries = sorted((x, i) for i, x in enumerate(queries))
        ans = [-1] * m
        pq: list[tuple[int, int]] = []
        i = 0
        for x, j in sorted_queries:
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
    intervals: list[list[int]] = deserialize("List[List[int]]", read_line())
    queries: list[int] = deserialize("List[int]", read_line())
    ans = Solution().minInterval(intervals, queries)

    print("\noutput:", serialize(ans))
