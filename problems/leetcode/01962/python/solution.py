# Created by shiyang07ca at 2023/12/23 00:28
# leetgo: dev
# https://leetcode.cn/problems/remove-stones-to-minimize-the-total/

from typing import *
from leetgo_py import *

from heapq import *
from math import *

# @lc code=begin


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        for p in piles:
            heappush(h, -p)
        for _ in range(k):
            heapreplace(h, h[0] + (-h[0] // 2))
        return -sum(h)


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minStoneSum(piles, k)

    print("\noutput:", serialize(ans))
