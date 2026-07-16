# Created by shiyang07ca at 2023/12/08 21:37
# leetgo: dev
# https://leetcode.cn/problems/maximum-earnings-from-taxi/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-earnings-from-taxi/
    def maxTaxiEarnings1(self, n: int, rides: List[List[int]]) -> int:
        groups = defaultdict(list)
        for start, end, tip in rides:
            groups[end].append((start, end - start + tip))

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i == 1:
                return 0
            return max(dfs(i - 1), max((dfs(s) + t for s, t in groups[i]), default=0))

        return dfs(n)

    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        ends = [r[1] for r in rides]
        f = [0] * (len(rides) + 1)
        for i, (st, ed, p) in enumerate(rides, 1):
            j = bisect_right(ends, st, hi=i - 1)
            f[i] = max(f[i - 1], f[j] + ed - st + p)

        return f[-1]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rides: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTaxiEarnings(n, rides)

    print("\noutput:", serialize(ans))
