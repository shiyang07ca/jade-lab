# Created by shiyang07ca at 2023/09/15 00:14
# leetgo: dev
# https://leetcode.cn/problems/WHnhjV/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            gem[y] += gem[x] // 2
            gem[x] -= gem[x] // 2
        return max(gem) - min(gem)


# @lc code=end

if __name__ == "__main__":
    gem: List[int] = deserialize("List[int]", read_line())
    operations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().giveGem(gem, operations)

    print("\noutput:", serialize(ans))
