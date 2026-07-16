# Created by shiyang07ca at 2024/04/08 21:34
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/solutions/1005398/on-zuo-fa-by-endlesscheng-l7yi/
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(set(nums))  # 去重排序
        ans = left = 0
        for i, x in enumerate(a):
            while a[left] < x - n + 1:  # a[left] 不在窗口内
                left += 1
            ans = max(ans, i - left + 1)
        return n - ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums)

    print("\noutput:", serialize(ans))
