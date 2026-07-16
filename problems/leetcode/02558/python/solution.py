# Created by shiyang07ca at 2023/10/28 20:42
# leetgo: dev
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile/

from heapq import *
from math import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gs = []
        for g in gifts:
            heappush(gs, -g)
        for _ in range(k):
            heapreplace(gs, -floor(sqrt(-gs[0])))
        return -sum(gs)


# @lc code=end

if __name__ == "__main__":
    gifts: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().pickGifts(gifts, k)

    print("\noutput:", serialize(ans))
