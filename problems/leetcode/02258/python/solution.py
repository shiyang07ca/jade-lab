# Created by shiyang07ca at 2023/11/09 13:11
# leetgo: dev
# https://leetcode.cn/problems/escape-the-spreading-fire/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/escape-the-spreading-fire/
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 返回能否在初始位置停留 t 分钟，并安全到达安全屋
        def check(t: int) -> bool:
            f = [
                (i, j)
                for i, row in enumerate(grid)
                for j, x in enumerate(row)
                if x == 1
            ]
            on_fire = set(f)  # 标记着火的位置

            def spread_fire():
                # 火的 BFS
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if (
                            0 <= x < m
                            and 0 <= y < n
                            and grid[x][y] == 0
                            and (x, y) not in on_fire
                        ):
                            on_fire.add((x, y))  # 标记着火的位置
                            f.append((x, y))

            while t and f:  # 如果火无法扩散就提前退出
                spread_fire()  # 火扩散
                t -= 1
            if (0, 0) in on_fire:
                return False  # 起点着火，寄

            # 人的 BFS
            q = [(0, 0)]
            vis = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) in on_fire:
                        continue  # 人走到这个位置后，火也扩散到了这个位置
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if (
                            0 <= x < m
                            and 0 <= y < n
                            and grid[x][y] == 0
                            and (x, y) not in on_fire
                            and (x, y) not in vis
                        ):
                            if x == m - 1 and y == n - 1:
                                return True  # 我们安全了…暂时。
                            vis.add((x, y))  # 避免反复访问同一个位置
                            q.append((x, y))
                spread_fire()  # 火扩散
            return False  # 人被火烧到，或者没有可以到达安全屋的路

        # 这里我用开区间二分（其它写法也可以）
        left = -1
        right = m * n + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left if left < m * n else 10**9


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumMinutes(grid)

    print("\noutput:", serialize(ans))
