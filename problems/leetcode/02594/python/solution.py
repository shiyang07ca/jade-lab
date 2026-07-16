# Created by shiyang07ca at 2023/09/07 12:59
# leetgo: dev
# https://leetcode.cn/problems/minimum-time-to-repair-cars/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Binary Search


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-time-to-repair-cars/solutions/2430475/python3javacgotypescript-yi-ti-yi-jie-er-f96a/
    def repairCars1(self, ranks: List[int], cars: int) -> int:
        def check(t: int) -> bool:
            return sum(int(sqrt(t // r)) for r in ranks) >= cars

        return bisect_left(range(ranks[0] * cars * cars), True, key=check)

    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(t: int) -> bool:
            return sum(int(sqrt(t // r)) for r in ranks) >= cars

        l, r = 0, ranks[0] * cars * cars
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    ranks: List[int] = deserialize("List[int]", read_line())
    cars: int = deserialize("int", read_line())
    ans = Solution().repairCars(ranks, cars)

    print("\noutput:", serialize(ans))
