# Created by shiyang07ca at 2024/03/13 21:36
# leetgo: dev
# https://leetcode.cn/problems/maximum-odd-binary-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a, b = s.count("0"), s.count("1")
        return (b - 1) * "1" + a * "0" + "1"


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumOddBinaryNumber(s)

    print("\noutput:", serialize(ans))
