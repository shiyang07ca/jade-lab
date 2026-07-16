# Created by shiyang07ca at 2024/10/19 11:39
# leetgo: dev
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/solutions/2819086/cong-zuo-dao-you-cao-zuo-jian-ji-xie-fa-yzcde/
    def minOperations(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if x == k % 2:  # 必须操作
                k += 1
        return k


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
