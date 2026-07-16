# Created by shiyang07ca at 2023/08/23 13:40
# leetgo: dev
# https://leetcode.cn/problems/count-pairs-of-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    # 链接：https://leetcode.cn/problems/count-pairs-of-nodes/solutions/2400682/ji-bai-100cong-shuang-zhi-zhen-dao-zhong-yhze/
    def countPairs(
        self, n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        # deg[i] 表示与点 i 相连的边的数目
        deg = [0] * (n + 1)  # 节点编号从 1 到 n
        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
        # 统计每条边的出现次数，注意 1-2 和 2-1 算同一条边
        cnt_e = Counter(tuple(sorted(e)) for e in edges)

        ans = [0] * len(queries)
        sorted_deg = sorted(deg)  # 排序，为了双指针
        for j, q in enumerate(queries):
            left, right = 1, n  # 相向双指针
            while left < right:
                if sorted_deg[left] + sorted_deg[right] <= q:
                    left += 1
                else:
                    ans[j] += right - left
                    right -= 1
            for (x, y), c in cnt_e.items():
                if q < deg[x] + deg[y] <= q + c:
                    ans[j] -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countPairs(n, edges, queries)

    print("\noutput:", serialize(ans))
