# Created by shiyang07ca at 2023/12/06 20:54
# leetgo: dev
# https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cnt = [0] * n
        for start, end in trips:

            def dfs(x: int, fa: int) -> bool:
                if x == end:
                    cnt[x] += 1
                    return True  # 找到 end
                for y in g[x]:
                    if y != fa and dfs(y, x):
                        cnt[x] += 1  # x 是 end 的祖先节点，也就在路径上
                        return True
                return False  # 未找到 end

            dfs(start, -1)

        # 类似 337. 打家劫舍 III
        def dfs(x: int, fa: int) -> (int, int):
            not_halve = price[x] * cnt[x]  # x 不变
            halve = not_halve // 2  # x 减半
            for y in g[x]:
                if y != fa:
                    nh, h = dfs(y, x)  # 计算 y 不变/减半的最小价值总和
                    not_halve += min(nh, h)  # x 不变，那么 y 可以不变或者减半，取这两种情况的最小值
                    halve += nh  # x 减半，那么 y 只能不变
            return not_halve, halve

        return min(dfs(0, -1))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    price: List[int] = deserialize("List[int]", read_line())
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotalPrice(n, edges, price, trips)

    print("\noutput:", serialize(ans))
