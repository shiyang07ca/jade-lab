# Created by shiyang07ca at 2024/02/28 13:07
# leetgo: dev
# https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/2259983/tan-xin-jian-ji-xie-fa-pythonjavacgo-by-5svh1/
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1):  # 从最后一个非叶节点开始算
            ans += abs(cost[i * 2 - 1] - cost[i * 2])  # 两个子节点变成一样的
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2])  # 累加路径和
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrements(n, cost)

    print("\noutput:", serialize(ans))
