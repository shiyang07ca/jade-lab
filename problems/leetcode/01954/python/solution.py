from __future__ import annotations

# Created by shiyang07ca at 2023/12/24 14:13
# leetgo: dev
# https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/solutions/2577655/python3javacgotypescript-yi-ti-shuang-ji-jtwk/
    def minimumPerimeter(self, neededApples: int) -> int:
        l, r = 1, 100000
        while l < r:
            mid = (l + r) >> 1
            if 2 * mid * (mid + 1) * (2 * mid + 1) >= neededApples:
                r = mid
            else:
                l = mid + 1
        return l * 8


# @lc code=end

if __name__ == "__main__":
    neededApples: int = deserialize("int", read_line())
    ans = Solution().minimumPerimeter(neededApples)

    print("\noutput:", serialize(ans))
