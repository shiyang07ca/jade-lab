# Created by shiyang07ca at 2024/03/19 00:00
# leetgo: dev
# https://leetcode.cn/problems/maximum-score-of-a-good-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Two Pointers


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-score-of-a-good-subarray/solutions/2695415/liang-chong-fang-fa-dan-diao-zhan-shuang-24zl/
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = min_h = nums[k]
        i = j = k
        for _ in range(n - 1):
            if j == n - 1 or i and nums[i - 1] > nums[j + 1]:
                i -= 1
                min_h = min(min_h, nums[i])
            else:
                j += 1
                min_h = min(min_h, nums[j])
            ans = max(ans, min_h * (j - i + 1))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumScore(nums, k)

    print("\noutput:", serialize(ans))
