# Created by shiyang07ca at 2023/10/17 22:19
# leetgo: dev
# https://leetcode.cn/problems/sum-multiples/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for x in range(1, n + 1):
            if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
                ans += x
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().sumOfMultiples(n)

    print("\noutput:", serialize(ans))
