from __future__ import annotations

# Created by shiyang07ca at 2024/05/14 00:01
# leetgo: dev
# https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/
from typing import Counter

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/solutions/1427626/ha-xi-biao-tan-xin-by-endlesscheng-tgtf/
    def minimumRounds(self, tasks: list[int]) -> int:
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())


# @lc code=end

if __name__ == "__main__":
    tasks: list[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRounds(tasks)
    print("\noutput:", serialize(ans, "integer"))
