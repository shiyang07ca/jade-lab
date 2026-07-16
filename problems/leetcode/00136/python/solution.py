# Created by shiyang07ca at 2023/10/14 00:02
# leetgo: dev
# https://leetcode.cn/problems/single-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for n, c in cnt.items():
            if c == 1:
                return n


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
