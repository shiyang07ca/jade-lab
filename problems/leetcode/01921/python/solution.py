from __future__ import annotations

import math
from heapq import heapify, heappop

# Created by shiyang07ca at 2023/09/03 00:47
# leetgo: dev
# https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def eliminateMaximum1(self, dist: list[int], speed: list[int]) -> int:
        ans = 0
        time = [math.ceil(d / s) for d, s in zip(dist, speed)]
        heapify(time)
        while time and time[0] > ans:
            heappop(time)
            ans += 1
        return ans

    # 链接：https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/solutions/857961/xiao-mie-guai-wu-de-zui-da-shu-liang-by-0ou2p/
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        arrivalTimes = sorted(
            [
                (monsterDist - 1) // monsterSpeed + 1
                for monsterDist, monsterSpeed in zip(dist, speed)
            ]
        )
        for attackTime, arrivalTime in enumerate(arrivalTimes):
            if arrivalTime <= attackTime:
                return attackTime
        return len(arrivalTimes)


# @lc code=end

if __name__ == "__main__":
    dist: list[int] = deserialize("List[int]", read_line())
    speed: list[int] = deserialize("List[int]", read_line())
    ans = Solution().eliminateMaximum(dist, speed)

    print("\noutput:", serialize(ans))
