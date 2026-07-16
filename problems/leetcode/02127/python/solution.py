# Created by shiyang07ca at 2023/11/01 23:17
# leetgo: dev
# https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        for f in favorite:
            deg[f] += 1  # 统计基环树每个节点的入度

        rg = [[] for _ in range(n)]  # 反图
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:  # 拓扑排序，剪掉图上所有树枝
            x = q.popleft()
            y = favorite[x]  # x 只有一条出边
            rg[y].append(x)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        # 通过反图 rg 寻找树枝上最深的链
        def rdfs(x: int) -> int:
            max_depth = 1
            for son in rg[x]:
                max_depth = max(max_depth, rdfs(son) + 1)
            return max_depth

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0:
                continue

            # 遍历基环上的点
            deg[i] = 0  # 将基环上的点的入度标记为 0，避免重复访问
            ring_size = 1  # 基环长度
            x = favorite[i]
            while x != i:
                deg[x] = 0  # 将基环上的点的入度标记为 0，避免重复访问
                ring_size += 1
                x = favorite[x]

            if ring_size == 2:  # 基环长度为 2
                sum_chain_size += rdfs(i) + rdfs(favorite[i])  # 累加两条最长链的长度
            else:
                max_ring_size = max(max_ring_size, ring_size)  # 取所有基环长度的最大值
        return max(max_ring_size, sum_chain_size)


# @lc code=end

if __name__ == "__main__":
    favorite: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumInvitations(favorite)

    print("\noutput:", serialize(ans))
