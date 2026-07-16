# Created by shiyang07ca at 2023/10/20 00:01
# leetgo: dev
# https://leetcode.cn/problems/categorize-box-according-to-criteria/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = (
            any([length >= 10**4, width >= 10**4, height >= 10**4])
            or (length * width * height) >= 10**9
        )
        heavy = mass >= 100
        if not bulky and not heavy:
            return "Neither"
        elif bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        else:
            return "Heavy"


# @lc code=end

if __name__ == "__main__":
    length: int = deserialize("int", read_line())
    width: int = deserialize("int", read_line())
    height: int = deserialize("int", read_line())
    mass: int = deserialize("int", read_line())
    ans = Solution().categorizeBox(length, width, height, mass)

    print("\noutput:", serialize(ans))
