# Created by shiyang07ca at 2023/10/27 13:20
# leetgo: dev
# https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
from itertools import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        MOD = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        a = max(
            horizontalCuts[0],
            *[b - a for a, b in pairwise(horizontalCuts)],
            h - horizontalCuts[-1],
        )
        b = max(
            verticalCuts[0],
            *[b - a for a, b in pairwise(verticalCuts)],
            w - verticalCuts[-1],
        )
        return a * b % MOD


# @lc code=end

if __name__ == "__main__":
    h: int = deserialize("int", read_line())
    w: int = deserialize("int", read_line())
    horizontalCuts: List[int] = deserialize("List[int]", read_line())
    verticalCuts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(h, w, horizontalCuts, verticalCuts)

    print("\noutput:", serialize(ans))
