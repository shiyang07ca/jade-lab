# Created by shiyang07ca at 2024/03/23 07:15
# leetgo: dev
# https://leetcode.cn/problems/count-distinct-numbers-on-board/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().distinctIntegers(n)

    print("\noutput:", serialize(ans))
