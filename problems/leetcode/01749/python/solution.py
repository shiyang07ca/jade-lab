# Created by shiyang07ca at 2023/08/08 09:36
# leetgo: dev
# https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxAbsoluteSum1(self, nums: List[int]) -> int:
        ans = abs(nums[0])
        n = len(nums)
        if n == 1:
            return ans

        pre0 = pre1 = 0
        if nums[0] > 0:
            pre0 = nums[0]
        else:
            pre1 = nums[0]

        for x in nums[1:]:
            if x > 0:
                pre0 += x
                pre1 = min(0, pre1 + x)
            elif x < 0:
                pre1 += x
                pre0 = max(0, pre0 + x)
            ans = max(ans, pre0, abs(pre1))
        return ans

    # 链接：https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/solutions/2377930/liang-chong-fang-fa-dong-tai-gui-hua-qia-dczr/
    def maxAbsoluteSum2(self, nums: List[int]) -> int:
        ans = f_max = f_min = 0
        for x in nums:
            f_max = max(f_max, 0) + x
            f_min = min(f_min, 0) + x
            ans = max(ans, f_max, -f_min)
        return ans

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        return max(s) - min(s)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxAbsoluteSum(nums)

    print("\noutput:", serialize(ans))
