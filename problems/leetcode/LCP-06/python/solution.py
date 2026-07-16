# Created by shiyang07ca at 2023/09/20 10:18
# leetgo: dev
# https://leetcode.cn/problems/na-ying-bi/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((c - 1) // 2 + 1 for c in coins)


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCount(coins)

    print("\noutput:", serialize(ans))
