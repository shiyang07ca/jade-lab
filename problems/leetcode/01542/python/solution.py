# Created by shiyang07ca at 2024/05/20 23:23
# leetgo: dev
# https://leetcode.cn/problems/find-longest-awesome-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-longest-awesome-substring/solutions/2773468/qian-zhui-yi-huo-he-fu-lei-si-ti-mu-pyth-j8lx/
    def longestAwesome(self, s: str) -> int:
        D = 10  # s 中的字符种类数
        n = len(s)
        pos = [n] * (1 << D)  # n 表示没有找到异或前缀和
        pos[0] = -1  # pre[-1] = 0
        ans = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(
                ans,
                i - pos[pre],  # 偶数
                max(i - pos[pre ^ (1 << d)] for d in range(D)),  # 奇数
            )
            if pos[pre] == n:  # 首次遇到值为 pre 的前缀异或和，记录其下标 i
                pos[pre] = i
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestAwesome(s)
    print("\noutput:", serialize(ans, "integer"))
