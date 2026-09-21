from __future__ import annotations

# Created by shiyang07ca at 2024/01/27 19:10
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-alloys/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:
# tag: Binary Search


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-number-of-alloys/solutions/2621375/python3javacgotypescript-yi-ti-yi-jie-er-zghl/
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: list[list[int]],
        stock: list[int],
        cost: list[int],
    ) -> int:
        ans = 0
        for c in composition:
            l, r = 0, budget + stock[0]
            while l < r:
                mid = (l + r + 1) >> 1
                s = sum(max(0, mid * x - y) * z for x, y, z in zip(c, stock, cost))
                if s <= budget:
                    l = mid
                else:
                    r = mid - 1
            ans = max(ans, l)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    budget: int = deserialize("int", read_line())
    composition: list[list[int]] = deserialize("List[List[int]]", read_line())
    stock: list[int] = deserialize("List[int]", read_line())
    cost: list[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)

    print("\noutput:", serialize(ans))
