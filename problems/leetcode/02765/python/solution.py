# Created by shiyang07ca at 2024/01/23 00:02
# leetgo: dev
# https://leetcode.cn/problems/longest-alternating-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# template


class Solution:
    def alternatingSubarray1(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        i = 0
        while i < n:
            t = 1
            s = i
            j = i + 1
            while j < n and nums[i] - nums[j] == (-1) ** t:
                t += 1
                j += 1
                i += 1
            i = s + 1
            if t > 1:
                ans = max(ans, t)
        return ans

    # 链接：https://leetcode.cn/problems/longest-alternating-subarray/solutions/2615916/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-r57bz/
    """
    分组循环
    n = len(nums)
    i = 0
    while i < n:
        start = i
        while i < n and ...:
            i += 1
        # 从 start 到 i-1 是一组
        # 下一组从 i 开始，无需 i += 1
    """

    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1  # 直接跳过
                continue
            i0 = i  # 记录这一组的开始位置
            i += 2  # i 和 i+1 已经满足要求，从 i+2 开始判断
            while i < n and nums[i] == nums[i - 2]:
                i += 1
            # 从 i0 到 i-1 是满足题目要求的（并且无法再延长的）子数组
            ans = max(ans, i - i0)
            i -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().alternatingSubarray(nums)

    print("\noutput:", serialize(ans))
