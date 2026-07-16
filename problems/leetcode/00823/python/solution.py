# Created by shiyang07ca at 2023/08/29 09:02
# leetgo: dev
# https://leetcode.cn/problems/binary-trees-with-factors/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def numFactoredBinaryTrees1(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort()
        t = defaultdict(list)
        pos = {x: i for i, x in enumerate(arr)}

        for i, x in enumerate(arr):
            if x * x in pos:
                t[pos[x * x]].append((i, i))
            for j in range(i + 1, n):
                if x * arr[j] in pos:
                    t[pos[x * arr[j]]].append((i, j))

        @cache
        def dfs(i):
            ans = 1
            for a, b in t[i]:
                if a == b:
                    ans = (ans + dfs(a) * dfs(b)) % MOD
                else:
                    ans = (ans + dfs(a) * dfs(b) * 2) % MOD
            return ans

        return sum(dfs(i) for i in range(n)) % MOD

    # 链接：https://leetcode.cn/problems/binary-trees-with-factors/solutions/2416115/cong-ji-yi-hua-sou-suo-dao-di-tui-jiao-n-nbk6/
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        idx = {x: i for i, x in enumerate(arr)}

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            res = 1
            val = arr[i]
            for j in range(i):  # val 的因子一定比 val 小
                x = arr[j]
                if val % x == 0 and val // x in idx:  # 另一个因子 val/x 必须在 arr 中
                    res += dfs(j) * dfs(idx[val // x])
            return res

        return sum(dfs(i) for i in range(len(arr))) % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFactoredBinaryTrees(arr)

    print("\noutput:", serialize(ans))
