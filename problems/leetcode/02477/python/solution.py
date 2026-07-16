# Created by shiyang07ca at 2023/12/05 23:40
# leetgo: dev
# https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/solution/kao-lu-mei-tiao-bian-shang-zhi-shao-xu-y-uamv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


考虑每条边上至少需要多少辆车。

以 0 为根，设子树 x 的大小为 size，那么它到它父节点这条边的「流量」是 size，那
么就至少需要 ceil⌈size/seats⌉ 辆车。

累加除了 x=0 以外的值，就是答案。

"""


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        g = [[] for _ in range(len(roads) + 1)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa):
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)

            if x:
                nonlocal ans
                ans += (size + seats - 1) // seats
            return size

        dfs(0, -1)
        return ans


# @lc code=end

if __name__ == "__main__":
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    seats: int = deserialize("int", read_line())
    ans = Solution().minimumFuelCost(roads, seats)

    print("\noutput:", serialize(ans))
