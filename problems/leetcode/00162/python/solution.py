# Created by shiyang07ca at 2023/12/18 00:23
# leetgo: dev
# https://leetcode.cn/problems/find-peak-element/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # https://leetcode.cn/problems/find-peak-element/solutions/2570331/python3javacgotypescript-yi-ti-yi-jie-er-9xk5/?envType=daily-question&envId=2023-12-18
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeakElement(nums)

    print("\noutput:", serialize(ans))
