"""
# 拓扑排序
有向图的拓扑排序 Kahn's algorithm
https://oi-wiki.org/graph/topo/
https://cp-algorithms.com/graph/topological-sort.html

LC207 https://leetcode.cn/problems/course-schedule/  模版
LC2392//周赛308D https://leetcode.cn/problems/build-a-matrix-with-conditions/
LC2050 https://leetcode.cn/problems/parallel-courses-iii/description/

"""


def top_sort(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for x, y in edges:
        g[x - 1].append(y - 1)
        indeg[y - 1] += 1
    order = []  # 拓扑序
    q = deque(i for i, v in enumerate(indeg) if v == 0)
    while q:  # BFS，每个点当入度为 0 时放入拓扑序结果中
        x = q.popleft()
        order.append(x)
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return order if len(order) == n else None
