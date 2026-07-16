# Created by shiyang07ca at 2024/11/09 16:31
# leetgo: 1.4.10
# https://leetcode.cn/problems/bitwise-and-of-numbers-range/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: 位运算


class Solution:
    # 链接：https://leetcode.cn/problems/bitwise-and-of-numbers-range/solutions/538550/golang-yi-xing-suan-fa-by-endlesscheng-iw6y/
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        m = (left ^ right).bit_length()
        return left & ~((1 << m) - 1)


# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().rangeBitwiseAnd(left, right)
    print("\noutput:", serialize(ans, "integer"))
