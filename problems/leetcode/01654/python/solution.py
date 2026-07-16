# Created by shiyang07ca at 2023/08/30 13:27
# leetgo: dev
# https://leetcode.cn/problems/minimum-jumps-to-reach-home/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-jumps-to-reach-home/solutions/2417782/python3javacgotypescript-yi-ti-yi-jie-bf-yfk7/
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        s = set(forbidden)
        q = deque([(0, 1)])
        vis = {(0, 1)}
        ans = 0
        while q:
            for _ in range(len(q)):
                i, k = q.popleft()
                if i == x:
                    return ans
                nxt = [(i + a, 1)]
                if k & 1:
                    nxt.append((i - b, 0))
                for j, k in nxt:
                    if 0 <= j < 6000 and j not in s and (j, k) not in vis:
                        q.append((j, k))
                        vis.add((j, k))
            ans += 1
        return -1


# @lc code=end

if __name__ == "__main__":
    forbidden: List[int] = deserialize("List[int]", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minimumJumps(forbidden, a, b, x)

    print("\noutput:", serialize(ans))
