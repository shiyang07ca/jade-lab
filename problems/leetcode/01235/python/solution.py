# Created by shiyang07ca at 2024/05/04 11:45
# leetgo: dev
# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    def jobScheduling1(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        inv = sorted(zip(endTime, startTime, profit))
        ends = [i[0] for i in inv]
        dp = [0] * (len(inv) + 1)
        for i, (end, start, p) in enumerate(inv, 1):
            j = bisect_right(ends, start, hi=i - 1)
            # dp[i] 表示 当前 i 位置的最大利润，有两种选择，
            # 选 i 位置 + dp[j]，或者选择 i - 1 位置的最大利润，两者取最大值。
            # j 表示大于 target(start) 的下界, 因此应该将j - 1，又因为是从1
            # 开始循环，因此需要加 1，dp[j - 1 + 1]
            dp[i] = max(dp[i - 1], dp[j] + p)
        return dp[-1]

    # 链接：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))  # 按照结束时间排序
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_left(jobs, (st + 1,), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
            # 状态转移中，为什么是 j 不是 j+1：上面算的是 > st，-1 后得到 <= st，但由于还要 +1，抵消了
            f[i + 1] = max(f[i], f[j] + p)
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
