# Created by shiyang07ca at 2026/10/01 01:48
# leetgo: 1.4.17
# https://leetcode.cn/problems/dota2-senate/

from collections import deque
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 两个队列分别保存两派未来的行动时间；每次让最早行动的双方相遇，时间较早者淘汰对方并进入下一轮。
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, party in enumerate(senate):
            if party == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # R 先行动，禁止 D；R 下一轮继续行动
                radiant.append(r + n)
            else:
                # D 先行动，禁止 R；D 下一轮继续行动
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"


# @lc code=end

if __name__ == "__main__":
    senate: str = deserialize("str", read_line())
    ans = Solution().predictPartyVictory(senate)
    print("\noutput:", serialize(ans, "string"))
