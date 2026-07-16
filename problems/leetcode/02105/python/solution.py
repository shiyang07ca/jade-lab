# Created by shiyang07ca at 2024/05/10 23:23
# leetgo: dev
# https://leetcode.cn/problems/watering-plants-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/watering-plants-ii/solutions/1153072/shuang-zhi-zhen-mo-ni-by-endlesscheng-9l76/
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        a, b = capacityA, capacityB
        i, j = 0, len(plants) - 1
        while i < j:
            # Alice 给植物 i 浇水
            if a < plants[i]:
                # 没有足够的水，重新灌满水罐
                ans += 1
                a = capacityA
            a -= plants[i]
            i += 1
            # Bob 给植物 j 浇水
            if b < plants[j]:
                # 没有足够的水，重新灌满水罐
                ans += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        # Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水
        if i == j and max(a, b) < plants[i]:
            # 没有足够的水，重新灌满水罐
            ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacityA: int = deserialize("int", read_line())
    capacityB: int = deserialize("int", read_line())
    ans = Solution().minimumRefill(plants, capacityA, capacityB)
    print("\noutput:", serialize(ans, "integer"))
