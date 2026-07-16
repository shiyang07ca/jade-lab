# Created by shiyang07ca at 2023/11/21 13:46
# leetgo: dev
# https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# 链接：https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        i = ans = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                ans += 1
                i += 1
            else:
                i += 2
        ans += (n - ans) % 2
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDeletion(nums)

    print("\noutput:", serialize(ans))
