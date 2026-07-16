# Created by shiyang07ca at 2023/11/11 10:33
# leetgo: dev
# https://leetcode.cn/problems/couples-holding-hands/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/couples-holding-hands/submissions/
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(row) >> 1
        p = list(range(n))
        for i in range(0, len(row), 2):
            a, b = row[i] >> 1, row[i + 1] >> 1
            p[find(a)] = find(b)
        return n - sum(i == find(i) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    row: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSwapsCouples(row)

    print("\noutput:", serialize(ans))
