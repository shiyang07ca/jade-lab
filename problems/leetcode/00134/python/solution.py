# Created by shiyang07ca at 2025/02/04 13:21
# leetgo: 1.4.13
# https://leetcode.cn/problems/gas-station/

from typing import *

from leetgo_py import *

# @lc code=begin

# TODO:
# tag: greedy, array


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 链接：https://leetcode.cn/problems/gas-station/solutions/2933132/yong-zhe-xian-tu-zhi-guan-li-jie-pythonj-qccr/
        ans = min_s = s = 0  # s 表示油量，min_s 表示最小油量
        for i, (g, c) in enumerate(zip(gas, cost)):
            s += g - c  # 在 i 处加油，然后从 i 到 i+1
            if s < min_s:
                min_s = s  # 更新最小油量
                ans = i + 1  # 注意 s 减去 c 之后，汽车在 i+1 而不是 i
        # 循环结束后，s 即为 gas 之和减去 cost 之和
        return -1 if s < 0 else ans


# @lc code=end

if __name__ == "__main__":
    gas: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canCompleteCircuit(gas, cost)
    print("\noutput:", serialize(ans, "integer"))
