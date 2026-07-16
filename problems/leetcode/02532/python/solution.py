# Created by shiyang07ca at 2023/07/07 09:36
# leetgo: dev
# https://leetcode.cn/problems/time-to-cross-a-bridge/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/time-to-cross-a-bridge/solutions/2050900/by-endlesscheng-nzqo/
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda t: t[0] + t[2])  # 稳定排序
        cur = 0
        workL, waitL, waitR, workR = (
            [],
            [[-i, 0] for i in range(k - 1, -1, -1)],
            [],
            [],
        )  # 下标越大效率越低
        while n:
            while workL and workL[0][0] <= cur:
                p = heappop(workL)
                p[0], p[1] = p[1], p[0]
                heappush(waitL, p)  # 左边完成放箱
            while workR and workR[0][0] <= cur:
                p = heappop(workR)
                p[0], p[1] = p[1], p[0]
                heappush(waitR, p)  # 右边完成搬箱
            if waitR:  # 右边过桥，注意加到 waitR 中的都是 <= cur 的（下同）
                p = heappop(waitR)
                cur += time[-p[0]][2]
                p[1] = p[0]
                p[0] = cur + time[-p[0]][3]
                heappush(workL, p)  # 放箱
            elif waitL:  # 左边过桥
                p = heappop(waitL)
                cur += time[-p[0]][0]
                p[1] = p[0]
                p[0] = cur + time[-p[0]][1]
                heappush(workR, p)  # 搬箱
                n -= 1
            elif len(workL) == 0:
                cur = workR[0][0]  # cur 过小，找个最小的放箱/搬箱完成时间来更新 cur
            elif len(workR) == 0:
                cur = workL[0][0]
            else:
                cur = min(workL[0][0], workR[0][0])
        while workR:
            t, i = heappop(workR)  # 右边完成搬箱
            # 如果没有排队，直接过桥；否则由于无论谁先过桥，最终完成时间都一样，所以也可以直接计算
            cur = max(t, cur) + time[-i][2]
        return cur  # 最后一个过桥的时间


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    time: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findCrossingTime(n, k, time)

    print("\noutput:", serialize(ans))
