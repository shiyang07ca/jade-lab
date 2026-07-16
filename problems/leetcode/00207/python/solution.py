# Created by shiyang07ca at 2023/09/09 12:40
# leetgo: dev
# https://leetcode.cn/problems/course-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: Topological Sort
# template


class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for y, x in edges:
            g[x].append(y)
            indeg[y] += 1
        order = []  # 拓扑序
        q = deque(i for i, v in enumerate(indeg) if v == 0)
        while q:  # BFS，每个点当入度为 0 时放入拓扑序结果中
            x = q.popleft()
            order.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        return len(order) == n


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)

    print("\noutput:", serialize(ans))
