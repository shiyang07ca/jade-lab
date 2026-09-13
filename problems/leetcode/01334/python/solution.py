from __future__ import annotations

from functools import cache
from sys import maxsize as inf

# Created by shiyang07ca at 2023/11/14 13:20
# leetgo: dev
# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:
# tag: dfs
# template


# 链接：https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        w = [[inf] * n for _ in range(n)]
        for x, y, wt in edges:
            w[x][y] = w[y][x] = wt

        @cache
        def dfs(k: int, i: int, j: int) -> int:
            if k < 0:  # 递归边界
                return w[i][j]
            return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

        ans = 0
        min_cnt = inf
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j != i and dfs(n - 1, i, j) <= distanceThreshold:
                    cnt += 1
            if cnt <= min_cnt:  # 相等时取最大的 i
                min_cnt = cnt
                ans = i
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: list[list[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)

    print("\noutput:", serialize(ans))
