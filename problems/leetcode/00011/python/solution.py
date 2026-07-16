# Created by shiyang07ca at 2024/11/11 08:59
# leetgo: 1.4.10
# https://leetcode.cn/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/container-with-most-water/solutions/1974355/by-endlesscheng-f0xz/
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                # height[left] 与右边的任意线段都无法组成一个比 ans 更大的面积
                left += 1
            else:
                # height[right] 与左边的任意线段都无法组成一个比 ans 更大的面积
                right -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))
