# Created by shiyang07ca at 2023/10/16 13:15
# leetgo: dev
# https://leetcode.cn/problems/single-number-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/single-number-iii/solutions/
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = reduce(xor, nums)
        lowbit = xor_all & -xor_all
        ans = [0, 0]
        for x in nums:
            ans[(x & lowbit) != 0] ^= x  # 分组异或
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
