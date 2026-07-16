# Created by shiyang07ca at 2024/05/30 00:12
# leetgo: dev
# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/solutions/2585801/fen-lei-tao-lun-jian-ji-xie-fa-pythonjav-671l/
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += 1
            if i + 1 == len(s) or ch != s[i + 1]:
                groups[ch].append(cnt)  # 统计连续字符长度
                cnt = 0

        ans = 0
        for a in groups.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

        return ans if ans else -1


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLength(s)
    print("\noutput:", serialize(ans, "integer"))
