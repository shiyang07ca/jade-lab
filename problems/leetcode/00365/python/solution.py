# Created by shiyang07ca at 2024/01/28 11:32
# leetgo: dev
# https://leetcode.cn/problems/water-and-jug-problem/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/water-and-jug-problem/solutions/2622442/python3javacgo-yi-ti-yi-jie-dfsqing-xi-t-j4lg/
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def dfs(i: int, j: int) -> bool:
            if (i, j) in vis:
                return False
            vis.add((i, j))
            if i == z or j == z or i + j == z:
                return True
            if dfs(x, j) or dfs(i, y) or dfs(0, j) or dfs(i, 0):
                return True
            a = min(i, y - j)
            b = min(j, x - i)
            return dfs(i - a, j + a) or dfs(i + b, j - b)

        vis = set()
        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    jug1Capacity: int = deserialize("int", read_line())
    jug2Capacity: int = deserialize("int", read_line())
    targetCapacity: int = deserialize("int", read_line())
    ans = Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)

    print("\noutput:", serialize(ans))
