# Created by shiyang07ca at 2023/11/16 00:16
# leetgo: dev
# https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        l = 0
        r = 1
        n = len(nums)
        while l < n:
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
                continue
            while r < n and nums[r] <= threshold and nums[r] % 2 != nums[r - 1] % 2:
                r += 1
            else:
                ans = max(ans, r - l)
                l = r
                r += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().longestAlternatingSubarray(nums, threshold)

    print("\noutput:", serialize(ans))
