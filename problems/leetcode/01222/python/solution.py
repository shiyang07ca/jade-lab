# Created by shiyang07ca at 2023/09/14 09:30
# leetgo: dev
# https://leetcode.cn/problems/queens-that-can-attack-the-king/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def queensAttacktheKing1(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        ans = []
        for i, (x2, y2) in enumerate(queens):
            x1, y1 = king
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            if x1 != x2 and y1 != y2 and dx != dy:
                continue
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            while dx or dy:
                if dx != 0:
                    dx -= 1
                    x1 += 1
                if dy != 0:
                    dy -= 1
                    y1 += 1 if y1 < y2 else -1
                if [x1, y1] in queens:
                    break
            if (x1, y1) == (x2, y2):
                ans.append(queens[i])

        return ans

    # 链接：https://leetcode.cn/problems/queens-that-can-attack-the-king/
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        s = set(map(tuple, queens))
        ans = []
        for dx, dy in (
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ):
            x, y = king[0] + dx, king[1] + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in s:
                    ans.append([x, y])
                    break
                x += dx
                y += dy
        return ans


# @lc code=end

if __name__ == "__main__":
    queens: List[List[int]] = deserialize("List[List[int]]", read_line())
    king: List[int] = deserialize("List[int]", read_line())
    ans = Solution().queensAttacktheKing(queens, king)

    print("\noutput:", serialize(ans))
