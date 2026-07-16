# Created by shiyang07ca at 2024/02/02 00:22
# leetgo: dev
# https://leetcode.cn/problems/stone-game-vi/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/stone-game-vi/solutions/832500/python-tan-xin-by-qubenhao-0vr4/
    def stoneGameVI1(self, aliceValues: List[int], bobValues: List[int]) -> int:
        totalValues = [(a + b) for a, b in zip(aliceValues, bobValues)]
        totalValues.sort(reverse=True)
        # 所有Alice能拿到的石头的总价值，其中每个都多拿了Bob的对应石子,
        # 再减去 Bob 所有的石子，正好等于 Alic 拿的价值 - Bob 拿的价值
        ans = sum(totalValues[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0

    # 链接：https://leetcode.cn/problems/stone-game-vi/solutions/2628498/xiang-xi-jie-shi-wei-shi-yao-yao-an-zhao-0zsg/
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        pairs = sorted(zip(a, b), key=lambda p: -p[0] - p[1])
        diff = sum(x if i % 2 == 0 else -y for i, (x, y) in enumerate(pairs))
        return (diff > 0) - (diff < 0)


# @lc code=end

if __name__ == "__main__":
    aliceValues: List[int] = deserialize("List[int]", read_line())
    bobValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVI(aliceValues, bobValues)

    print("\noutput:", serialize(ans))
