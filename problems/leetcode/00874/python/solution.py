# Created by shiyang07ca at 2023/07/19 09:37
# leetgo: dev
# https://leetcode.cn/problems/walking-robot-simulation/

from collections import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = d = 0
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur = [0, 0]
        ox, oy = defaultdict(set), defaultdict(set)
        for o in obstacles:
            ox[o[0]].add(o[1])
            oy[o[1]].add(o[0])
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
                continue
            elif c == -2:
                d = (d - 1) % 4
                continue
            else:
                x, y = cur
                dx, dy = ds[d][0], ds[d][1]
                if dx == 0:
                    if x in ox:
                        for y in range(y + dy, y + dy * (c + 1), dy):
                            if y in ox[x]:
                                break
                            cur[1] = y
                    else:
                        cur[1] = y + dy * c
                if dy == 0:
                    if y in oy:
                        for x in range(x + dx, x + dx * (c + 1), dx):
                            if x in oy[y]:
                                break
                            cur[0] = x
                    else:
                        cur[0] = x + dx * c
            ans = max(ans, cur[0] ** 2 + cur[1] ** 2)
        return ans

    # 链接：https://leetcode.cn/problems/walking-robot-simulation/solutions/2349712/python3javacgotypescript-yi-ti-yi-jie-ha-ghjx/
    def robotSim2(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        s = {(x, y) for x, y in obstacles}
        ans = k = 0
        x = y = 0
        for c in commands:
            if c == -2:
                k = (k + 3) % 4
            elif c == -1:
                k = (k + 1) % 4
            else:
                for _ in range(c):
                    nx, ny = x + dirs[k], y + dirs[k + 1]
                    if (nx, ny) in s:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)
        return ans


# @lc code=end

if __name__ == "__main__":
    commands: List[int] = deserialize("List[int]", read_line())
    obstacles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().robotSim(commands, obstacles)

    print("\noutput:", serialize(ans))
