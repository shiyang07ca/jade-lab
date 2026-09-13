from __future__ import annotations

from collections import defaultdict
from functools import cache

# Created by shiyang07ca at 2024/03/15 22:30
# leetgo: dev
# https://leetcode.cn/problems/selling-pieces-of-wood/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    # 链接：https://leetcode.cn/problems/selling-pieces-of-wood/solutions/
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        @cache
        def dfs(h: int, w: int) -> int:
            ans = d[h].get(w, 0)
            for i in range(1, h // 2 + 1):
                ans = max(ans, dfs(i, w) + dfs(h - i, w))
            for i in range(1, w // 2 + 1):
                ans = max(ans, dfs(h, i) + dfs(h, w - i))
            return ans

        d = defaultdict(dict)
        for h, w, p in prices:
            d[h][w] = p
        return dfs(m, n)


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    prices: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sellingWood(m, n, prices)

    print("\noutput:", serialize(ans))
