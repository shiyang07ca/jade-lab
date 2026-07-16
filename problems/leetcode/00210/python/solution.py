# Created by shiyang07ca at 2023/09/10 13:23
# leetgo: dev
# https://leetcode.cn/problems/course-schedule-ii/

from typing import *
from collections import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
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
        return order if len(order) == n else []


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findOrder(numCourses, prerequisites)

    print("\noutput:", serialize(ans))
