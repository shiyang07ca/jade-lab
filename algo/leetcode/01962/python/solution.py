from __future__ import annotations

from heapq import heappush, heapreplace

# Created by shiyang07ca at 2023/12/23 00:28
# leetgo: dev
# https://leetcode.cn/problems/remove-stones-to-minimize-the-total/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        h = []
        for p in piles:
            heappush(h, -p)
        for _ in range(k):
            heapreplace(h, h[0] + (-h[0] // 2))
        return -sum(h)


# @lc code=end

if __name__ == "__main__":
    piles: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minStoneSum(piles, k)

    print("\noutput:", serialize(ans))
