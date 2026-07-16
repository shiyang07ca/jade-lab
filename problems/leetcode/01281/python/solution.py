# Created by shiyang07ca at 2023/08/09 08:04
# leetgo: dev
# https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = [int(c) for c in str(n)]
        a = 1
        for c in s:
            a *= c
        return a - sum(s)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().subtractProductAndSum(n)

    print("\noutput:", serialize(ans))
