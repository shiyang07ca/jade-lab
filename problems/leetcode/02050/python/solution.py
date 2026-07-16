# Created by shiyang07ca at 2023/07/28 12:44
# leetgo: dev
# https://leetcode.cn/problems/parallel-courses-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: Topological Sort
# template
# TODO


class Solution:
    # 链接：https://leetcode.cn/problems/parallel-courses-iii/solutions/2362108/python3javacgotypescript-yi-ti-yi-jie-tu-4nbv/
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = defaultdict(list)
        indeg = [0] * n
        for a, b in relations:
            g[a - 1].append(b - 1)
            indeg[b - 1] += 1
        q = deque()
        f = [0] * n
        ans = 0
        for i, (v, t) in enumerate(zip(indeg, time)):
            if v == 0:
                q.append(i)
                f[i] = t
                ans = max(ans, t)
        while q:
            i = q.popleft()
            for j in g[i]:
                f[j] = max(f[j], f[i] + time[j])
                ans = max(ans, f[j])
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return ans

    # 链接：https://leetcode.cn/problems/parallel-courses-iii/solutions/1063928/tuo-bu-pai-xu-dong-tai-gui-hua-by-endles-dph6/
    def minimumTime2(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n)]
        deg = [0] * n  # deg[i] 表示 i 的先修课的个数
        for x, y in relations:
            g[x - 1].append(y - 1)  # 建图
            deg[y - 1] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)  # 没有先修课
        f = [0] * n
        while q:
            x = q.popleft()  # x 出队，意味着 x 的所有先修课都上完了
            f[x] += time[x]  # 加上当前课程的时间，就得到了最终的 f[x]
            for y in g[x]:  # 遍历 x 的邻居 y
                f[y] = max(f[y], f[x])  # 更新 f[y] 的所有先修课程耗时的最大值
                deg[y] -= 1
                if deg[y] == 0:  # y 的先修课已上完
                    q.append(y)
        return max(f)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, relations, time)

    print("\noutput:", serialize(ans))
