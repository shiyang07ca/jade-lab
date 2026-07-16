# Created by shiyang07ca at 2024/02/29 00:08
# leetgo: dev
# https://leetcode.cn/problems/count-number-of-possible-root-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/count-number-of-possible-root-nodes/solutions/2147714/huan-gen-dppythonjavacgo-by-endlesscheng-ccwy/
    def rootCount(
        self, edges: List[List[int]], guesses: List[List[int]], k: int
    ) -> int:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        s = {(x, y) for x, y in guesses}  # guesses 转成哈希表 s

        ans = cnt0 = 0

        def dfs(x: int, fa: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y != fa:
                    cnt0 += (x, y) in s  # 以 0 为根时，猜对了
                    dfs(y, x)

        dfs(0, -1)

        def reroot(x: int, fa: int, cnt: int) -> None:
            nonlocal ans
            ans += cnt >= k  # 此时 cnt 就是以 x 为根时的猜对次数
            for y in g[x]:
                if y != fa:
                    reroot(y, x, cnt - ((x, y) in s) + ((y, x) in s))

        reroot(0, -1, cnt0)
        return ans


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    guesses: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().rootCount(edges, guesses, k)

    print("\noutput:", serialize(ans))
