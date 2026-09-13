from __future__ import annotations

# Created by shiyang07ca at 2023/09/12 08:11
# leetgo: dev
# https://leetcode.cn/problems/course-schedule-iv/
from collections import deque

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/course-schedule-iv/solutions/2417905/ke-cheng-biao-iv-by-leetcode-solution-mpc3/
    def checkIfPrerequisite(
        self, n: int, edges: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for x, y in edges:
            g[x].append(y)
            indeg[y] += 1
        q = deque(i for i, v in enumerate(indeg) if v == 0)
        is_pre = [[False] * n for _ in range(n)]
        while q:  # BFS，每个点当入度为 0 时放入拓扑序结果中
            x = q.popleft()
            for y in g[x]:
                is_pre[x][y] = True
                for i in range(n):
                    is_pre[i][y] = is_pre[i][y] or is_pre[i][x]
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)

        ans = []
        for x, y in queries:
            ans.append(is_pre[x][y])
        return ans


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: list[list[int]] = deserialize("List[List[int]]", read_line())
    queries: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkIfPrerequisite(numCourses, prerequisites, queries)

    print("\noutput:", serialize(ans))
