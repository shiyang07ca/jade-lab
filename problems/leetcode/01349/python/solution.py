# Created by shiyang07ca at 2023/12/26 00:11
# leetgo: dev
# https://leetcode.cn/problems/maximum-students-taking-exam/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Bit Manipulation, Dynamic Programming


class Solution:
    # https://leetcode.cn/problems/maximum-students-taking-exam/solutions/2580043/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-9y5k/
    def maxStudents(self, seats: List[List[str]]) -> int:
        a = [sum((c == ".") << j for j, c in enumerate(s)) for s in seats]

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == 0:
                lb = j & -j
                return dfs(i, j & ~(lb * 3)) + 1 if j else 0
            res = dfs(i - 1, a[i - 1])  # 第 i 排空着
            s = j
            while s:  # 枚举 j 的子集 s
                if (s & (s >> 1)) == 0:  # s 没有连续的 1
                    t = a[i - 1] & ~(s << 1 | s >> 1)
                    res = max(res, dfs(i - 1, t) + s.bit_count())
                s = (s - 1) & j
            return res

        return dfs(len(seats) - 1, a[-1])


# @lc code=end

if __name__ == "__main__":
    seats: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maxStudents(seats)

    print("\noutput:", serialize(ans))
