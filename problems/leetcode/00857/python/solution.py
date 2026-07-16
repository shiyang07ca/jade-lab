# Created by shiyang07ca at 2024/05/02 14:10
# leetgo: dev
# https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/solutions/1815856/yi-bu-bu-ti-shi-ru-he-si-kao-ci-ti-by-en-1p00/
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])  # 按照 r 值排序
        h = [-q for q, _ in pairs[:k]]  # 加负号变成最大堆
        heapify(h)
        sum_q = -sum(h)
        ans = sum_q * pairs[k - 1][1] / pairs[k - 1][0]  # 选 r 值最小的 k 名工人
        for q, w in pairs[k:]:  # 后面的工人 r 值更大
            if q < -h[0]:  # 但是 sum_q 可以变小，从而可能得到更优的答案
                sum_q += heapreplace(h, -q) + q  # 更新堆顶和 sum_q
                ans = min(ans, sum_q * w / q)
        return ans


# @lc code=end

if __name__ == "__main__":
    quality: List[int] = deserialize("List[int]", read_line())
    wage: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mincostToHireWorkers(quality, wage, k)
    print("\noutput:", serialize(ans, "double"))
