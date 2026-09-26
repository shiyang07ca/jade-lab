# Created by shiyang07ca at 2026/09/24 00:09
# leetgo: 1.4.17
# https://leetcode.cn/problems/minimum-genetic-mutation/

from typing import *

from leetgo_py import *

# @lc code=begin

"""
链接：https://leetcode.cn/problems/minimum-genetic-mutation/solutions/1474617/by-fuxuemingzhu-t1mv/

"""


# TODO
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = []
        queue.append((start, 0))
        while queue:
            current, steps = queue.pop(0)
            if current == end:
                return steps
            for i in range(len(current)):
                for c in "ACGT":
                    new = current[:i] + c + current[i + 1 :]
                    if new in bank and new != current:
                        queue.append((new, steps + 1))
                        bank.remove(new)
        return -1


# @lc code=end

if __name__ == "__main__":
    start: str = deserialize("str", read_line())
    end: str = deserialize("str", read_line())
    bank: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minMutation(start, end, bank)
    print("\noutput:", serialize(ans, "integer"))
