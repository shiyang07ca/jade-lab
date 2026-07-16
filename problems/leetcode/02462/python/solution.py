# Created by shiyang07ca at 2024/05/01 10:24
# leetgo: dev
# https://leetcode.cn/problems/total-cost-to-hire-k-workers/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/total-cost-to-hire-k-workers/solutions/1951938/liang-ge-zui-xiao-dui-mo-ni-by-endlessch-nagm/
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 + k > n:
            # 也可以 sum(nsmallest(k, costs))，但效率不如直接排序
            costs.sort()
            return sum(costs[:k])

        pre = costs[:candidates]
        suf = costs[-candidates:]
        heapify(pre)
        heapify(suf)

        ans = 0
        i = candidates
        j = n - 1 - candidates
        for _ in range(k):
            if pre[0] <= suf[0]:
                ans += heapreplace(pre, costs[i])
                i += 1
            else:
                ans += heapreplace(suf, costs[j])
                j -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    costs: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    candidates: int = deserialize("int", read_line())
    ans = Solution().totalCost(costs, k, candidates)
    print("\noutput:", serialize(ans, "long"))
