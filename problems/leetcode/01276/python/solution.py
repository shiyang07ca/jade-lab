# Created by shiyang07ca at 2023/12/25 00:04
# leetgo: dev
# https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numOfBurgers(self, n: int, m: int) -> List[int]:
        """
        x + y = m
        4x + 2y = n

        2x + 2y = 2m

        x = (n - 2m) // 2
        y = 2m - n // 2
        """
        if n - 2 * m >= 0 and (n - 2 * m) % 2 == 0 and (2 * m - n // 2) >= 0:
            return [(n - 2 * m) // 2, 2 * m - n // 2]
        return []


# @lc code=end

if __name__ == "__main__":
    tomatoSlices: int = deserialize("int", read_line())
    cheeseSlices: int = deserialize("int", read_line())
    ans = Solution().numOfBurgers(tomatoSlices, cheeseSlices)

    print("\noutput:", serialize(ans))
