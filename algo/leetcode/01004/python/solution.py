# Created by shiyang07ca at 2026/10/07 23:30
# leetgo: 1.4.17
# https://leetcode.cn/problems/max-consecutive-ones-iii/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        best_length = 0

        for right, value in enumerate(nums):
            # 1. 把右侧元素加入窗口。
            if value == 0:
                zero_count += 1

            # 2. 0 太多时，从左侧缩小窗口，直到合法。
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # 3. 当前窗口合法，更新最大长度。
            window_length = right - left + 1
            best_length = max(best_length, window_length)

        return best_length


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestOnes(nums, k)
    print("\noutput:", serialize(ans, "integer"))
