# Created by shiyang07ca at 2023/10/26 13:04
# leetgo: dev
# https://leetcode.cn/problems/count-the-digits-that-divide-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countDigits(self, num: int) -> int:
        d = num
        ans = 0
        while d:
            if num % (d % 10) == 0:
                ans += 1
            d //= 10
        return ans


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().countDigits(num)

    print("\noutput:", serialize(ans))
