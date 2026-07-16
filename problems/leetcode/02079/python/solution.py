# Created by shiyang07ca at 2024/05/08 00:04
# leetgo: dev
# https://leetcode.cn/problems/watering-plants/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        t = capacity
        for i, p in enumerate(plants):
            if t < p:
                ans += 2 * i
                t = capacity
            ans += 1
            t -= p

        return ans


# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().wateringPlants(plants, capacity)
    print("\noutput:", serialize(ans, "integer"))
