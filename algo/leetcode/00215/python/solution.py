# Created by shiyang07ca at 2026/10/21 22:56
# leetgo: 1.4.17
# https://leetcode.cn/problems/kth-largest-element-in-an-array/

import random

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 随机快速选择：期望时间 O(n)，最坏 O(n²)，额外空间 O(n)。
        while True:
            pivot = random.choice(nums)
            larger, equal, smaller = [], [], []

            for x in nums:
                if x > pivot:
                    larger.append(x)
                elif x == pivot:
                    equal.append(x)
                else:
                    smaller.append(x)

            # 只保留第 k 大所在的组，重复数字各占一个位置。
            if k <= len(larger):
                nums = larger
            elif k <= len(larger) + len(equal):
                return pivot
            else:
                # 排除前两组后，换算目标在较小组中的排名。
                k -= len(larger) + len(equal)
                nums = smaller

# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)
    print("\noutput:", serialize(ans, "integer"))
