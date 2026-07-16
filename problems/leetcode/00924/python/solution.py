# Created by shiyang07ca at 2024/04/16 00:00
# leetgo: dev
# https://leetcode.cn/problems/minimize-malware-spread/

from typing import *
from leetgo_py import *

# @lc code=begin


# TODO:
# tag: dfs


class Solution:
    # 链接：https://leetcode.cn/problems/minimize-malware-spread/solutions/2741790/zhi-bao-han-yi-ge-bei-gan-ran-jie-dian-d-ym39/
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)

        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal node_id, size
            size += 1
            # 按照状态机更新 node_id
            if node_id != -2 and x in st:
                node_id = x if node_id == -1 else -2
            for y, conn in enumerate(graph[x]):
                if conn and not vis[y]:
                    dfs(y)

        ans = -1
        max_size = 0
        for x in initial:
            if vis[x]:
                continue
            node_id = -1
            size = 0
            dfs(x)
            if node_id >= 0 and (size > max_size or size == max_size and node_id < ans):
                ans = node_id
                max_size = size
        return min(initial) if ans < 0 else ans


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    initial: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMalwareSpread(graph, initial)
    print("\noutput:", serialize(ans, "integer"))
