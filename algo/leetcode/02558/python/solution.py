from __future__ import annotations

# Created by shiyang07ca at 2023/10/28 20:42
# leetgo: dev
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile/
from heapq import heappush, heapreplace
from math import floor, sqrt

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gs = []
        for g in gifts:
            heappush(gs, -g)
        for _ in range(k):
            heapreplace(gs, -floor(sqrt(-gs[0])))
        return -sum(gs)


# @lc code=end

if __name__ == "__main__":
    gifts: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().pickGifts(gifts, k)

    print("\noutput:", serialize(ans))
