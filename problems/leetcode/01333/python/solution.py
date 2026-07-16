# Created by shiyang07ca at 2023/09/27 13:38
# leetgo: dev
# https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        ans = []
        for r in restaurants:
            if veganFriendly:
                if r[2] and r[3] <= maxPrice and r[4] <= maxDistance:
                    ans.append(r)
            elif r[3] <= maxPrice and r[4] <= maxDistance:
                ans.append(r)
        ans.sort(key=lambda x: [x[1], x[0]], reverse=True)
        return [e[0] for e in ans]


# @lc code=end

if __name__ == "__main__":
    restaurants: List[List[int]] = deserialize("List[List[int]]", read_line())
    veganFriendly: int = deserialize("int", read_line())
    maxPrice: int = deserialize("int", read_line())
    maxDistance: int = deserialize("int", read_line())
    ans = Solution().filterRestaurants(
        restaurants, veganFriendly, maxPrice, maxDistance
    )

    print("\noutput:", serialize(ans))
