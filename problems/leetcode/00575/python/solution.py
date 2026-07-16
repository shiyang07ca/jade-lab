# Created by shiyang07ca at 2024/06/02 02:40
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        cnt = len(Counter(candyType).keys())
        n = len(candyType) // 2
        return cnt if cnt < n else n


# @lc code=end

if __name__ == "__main__":
    candyType: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distributeCandies(candyType)
    print("\noutput:", serialize(ans, "integer"))
