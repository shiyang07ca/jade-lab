# Created by shiyang07ca at 2024/05/14 00:01
# leetgo: dev
# https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/solutions/1427626/ha-xi-biao-tan-xin-by-endlesscheng-tgtf/
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())


# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRounds(tasks)
    print("\noutput:", serialize(ans, "integer"))
