# Created by shiyang07ca at 2024/03/01 13:41
# leetgo: dev
# https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    # 链接：https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/solutions/1728735/by-endlesscheng-8y73/
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            if (
                i > 0
                and f[i - 1]
                and x == nums[i - 1]
                or i > 1
                and f[i - 2]
                and (
                    x == nums[i - 1] == nums[i - 2]
                    or x == nums[i - 1] + 1 == nums[i - 2] + 2
                )
            ):
                f[i + 1] = True
        return f[n]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validPartition(nums)

    print("\noutput:", serialize(ans))
