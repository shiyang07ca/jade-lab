# Created by shiyang07ca at 2024/03/05 13:20
# leetgo: dev
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp, graph


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/solutions/2668041/zai-ji-suan-zui-duan-lu-de-tong-shi-dpfu-g4f3/
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, d in roads:
            g[x].append((y, d))
            g[y].append((x, d))

        dis = [inf] * n
        dis[0] = 0
        f = [0] * n
        f[0] = 1
        h = [(0, 0)]
        while True:
            dx, x = heappop(h)
            if x == n - 1:
                # 不可能找到比 dis[-1] 更短，或者一样短的最短路了（注意本题边权都是正数）
                return f[-1]
            if dx > dis[x]:
                continue
            for y, d in g[x]:  # 尝试更新 x 的邻居的最短路
                new_dis = dx + d
                if new_dis < dis[y]:
                    # 就目前来说，最短路必须经过 x
                    dis[y] = new_dis
                    f[y] = f[x]
                    heappush(h, (new_dis, y))
                elif new_dis == dis[y]:
                    # 和之前求的最短路一样长
                    f[y] = (f[y] + f[x]) % 1_000_000_007


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)

    print("\noutput:", serialize(ans))
