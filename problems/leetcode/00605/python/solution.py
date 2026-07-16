# Created by shiyang07ca at 2023/09/29 12:06
# leetgo: dev
# https://leetcode.cn/problems/can-place-flowers/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        for i, x in enumerate(flowerbed):
            if n <= 0:
                break

            if (
                x == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == N - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                flowerbed[i] = 1

        return n <= 0

    # 链接：https://leetcode.cn/problems/can-place-flowers/
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1  # 种花！
                n -= 1
        return n <= 0


# @lc code=end

if __name__ == "__main__":
    flowerbed: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().canPlaceFlowers(flowerbed, n)

    print("\noutput:", serialize(ans))
