# Created by shiyang07ca at 2024/05/18 23:31
# leetgo: dev
# https://leetcode.cn/problems/find-the-maximum-divisibility-score/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        mx = -1
        ans = divisors[0]
        for d in divisors:
            c = 0
            for n in nums:
                if n % d == 0:
                    c += 1
            if c > mx:
                mx = c
                ans = d
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    divisors: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDivScore(nums, divisors)
    print("\noutput:", serialize(ans, "integer"))
