# Created by shiyang07ca at 2023/07/24 09:25
# leetgo: dev
# https://leetcode.cn/problems/jewels-and-stones/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for s in stones if s in jewels)


# @lc code=end

if __name__ == "__main__":
    jewels: str = deserialize("str", read_line())
    stones: str = deserialize("str", read_line())
    ans = Solution().numJewelsInStones(jewels, stones)

    print("\noutput:", serialize(ans))
