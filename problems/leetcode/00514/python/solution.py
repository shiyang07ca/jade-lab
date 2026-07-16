# Created by shiyang07ca at 2024/01/29 13:41
# leetgo: dev
# https://leetcode.cn/problems/freedom-trail/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/freedom-trail/solutions/2623534/onm-zuo-fa-cong-ji-yi-hua-sou-suo-dao-di-dnec/
    def findRotateSteps(self, s: str, t: str) -> int:
        s = [ord(c) - ord("a") for c in s]
        t = [ord(c) - ord("a") for c in t]
        n = len(s)

        # 先算出每个字母的最后一次出现的下标
        # 由于 s 是环形的，循环结束后的 pos 就刚好是 left[0]
        pos = [0] * 26  # 初始值不重要
        for i, c in enumerate(s):
            pos[c] = i
        # 计算每个 s[i] 左边 a-z 的最近下标（左边没有就从 n-1 往左找）
        left = [None] * n
        for i, c in enumerate(s):
            left[i] = pos[:]
            pos[c] = i  # 更新下标

        # 先算出每个字母的首次出现的下标
        # 由于 s 是环形的，循环结束后的 pos 就刚好是 right[n-1]
        for i in range(n - 1, -1, -1):
            pos[s[i]] = i
        # 计算每个 s[i] 右边 a-z 的最近下标（左边没有就从 0 往右找）
        right = [None] * n
        for i in range(n - 1, -1, -1):
            right[i] = pos[:]
            pos[s[i]] = i  # 更新下标

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(j: int, i: int) -> int:
            if j == len(t):
                return 0
            c = t[j]
            if s[i] == c:  # 无需旋转
                return dfs(j + 1, i)
            # 左边最近 or 右边最近，取最小值
            l, r = left[i][c], right[i][c]
            return min(
                dfs(j + 1, l) + (n - l + i if l > i else i - l),
                dfs(j + 1, r) + (n - i + r if r < i else r - i),
            )

        return dfs(0, 0) + len(t)


# @lc code=end

if __name__ == "__main__":
    ring: str = deserialize("str", read_line())
    key: str = deserialize("str", read_line())
    ans = Solution().findRotateSteps(ring, key)

    print("\noutput:", serialize(ans))
