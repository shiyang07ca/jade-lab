# Created by shiyang07ca at 2024/01/25 00:34
# leetgo: dev
# https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(n for i, n in enumerate(nums) if i.bit_count() == k)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().sumIndicesWithKSetBits(nums, k)

    print("\noutput:", serialize(ans))
