from __future__ import annotations

from functools import cache
from itertools import count

# Created by shiyang07ca at 2024/04/19 23:46
# leetgo: dev
# https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/solutions/2746611/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-gxd2/
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if j < 0:
                return 0
            res = (dfs(i, j - 1) + dist[j] + speed - 1) // speed * speed
            if i:
                res = min(res, dfs(i - 1, j - 1) + dist[j])
            return res

        for i in count(0):
            if dfs(i, len(dist) - 2) + dist[-1] <= speed * hoursBefore:
                return i
        raise RuntimeError("unreachable")


# @lc code=end

if __name__ == "__main__":
    dist: list[int] = deserialize("List[int]", read_line())
    speed: int = deserialize("int", read_line())
    hoursBefore: int = deserialize("int", read_line())
    ans = Solution().minSkips(dist, speed, hoursBefore)
    print("\noutput:", serialize(ans, "integer"))
