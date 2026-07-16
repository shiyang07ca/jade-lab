# Created by shiyang07ca at 2023/11/15 00:19
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-with-exactly-k-elements/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i in range(k):
            ans += nums[-1] + i
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximizeSum(nums, k)

    print("\noutput:", serialize(ans))
