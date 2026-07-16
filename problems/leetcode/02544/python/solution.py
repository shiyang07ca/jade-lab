# Created by shiyang07ca at 2023/07/13 10:04
# leetgo: dev
# https://leetcode.cn/problems/alternating-digit-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        op = 1
        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10
        for n in nums[::-1]:
            ans += op * n
            op *= -1
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().alternateDigitSum(n)

    print("\noutput:", serialize(ans))
