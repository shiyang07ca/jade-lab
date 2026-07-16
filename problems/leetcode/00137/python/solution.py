# Created by shiyang07ca at 2023/10/15 18:02
# leetgo: dev
# https://leetcode.cn/problems/single-number-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort()
        for i in range(0, n - 1, 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            cnt = Counter([a, b, c])
            for x, c in cnt.items():
                if c == 1:
                    return x

        return nums[n - 1]

    # 链接：https://leetcode.cn/problems/single-number-ii/
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            cnt1 = sum(x >> i & 1 for x in nums)
            ans |= cnt1 % 3 << i
        cnt1 = sum(x >> 31 & 1 for x in nums)
        return ans - (cnt1 % 3 << 31)  # 符号位


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
