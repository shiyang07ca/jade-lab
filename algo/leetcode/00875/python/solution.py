# Created by shiyang07ca at 2026/09/27 11:59
# leetgo: 1.4.17
# https://leetcode.cn/problems/koko-eating-bananas/

from typing import *

from leetgo_py import *

# @lc code=begin


# TODO
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, 10**9
        while left < right:
            mid = (left + right) // 2
            used = 0
            for p in piles[::-1]:
                # 每堆耗时
                used += p // mid + (1 if p % mid != 0 else 0)

            if used > h:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    h: int = deserialize("int", read_line())
    ans = Solution().minEatingSpeed(piles, h)
    print("\noutput:", serialize(ans, "integer"))
