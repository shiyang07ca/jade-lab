# Created by shiyang07ca at 2023/09/26 10:05
# leetgo: dev
# https://leetcode.cn/problems/pass-the-pillow/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time // (n - 1) % 2:
            return n - time % (n - 1)
        else:
            return time % (n - 1) + 1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().passThePillow(n, time)

    print("\noutput:", serialize(ans))
