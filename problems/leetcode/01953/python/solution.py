# Created by shiyang07ca at 2024/05/16 00:10
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/solutions/2779207/tan-xin-ju-ti-gou-zao-fang-an-pythonjava-3xyq/
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        m = max(milestones)
        return (s - m) * 2 + 1 if m > s - m + 1 else s


# @lc code=end

if __name__ == "__main__":
    milestones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfWeeks(milestones)
    print("\noutput:", serialize(ans, "long"))
