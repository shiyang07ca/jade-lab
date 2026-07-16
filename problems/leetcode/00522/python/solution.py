# Created by shiyang07ca at 2024/06/17 08:17
# leetgo: dev
# https://leetcode.cn/problems/longest-uncommon-subsequence-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/longest-uncommon-subsequence-ii/solutions/1627700/pythonjavatypescriptgo-mo-ni-by-himymben-1bsf/
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub_str(s1: str, s2: str) -> bool:
            if len(s2) < len(s1):
                return False
            i = j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s1)

        ans = -1
        for i, s in enumerate(strs):
            if len(s) > ans and all(
                not is_sub_str(s, s_) for j, s_ in enumerate(strs) if j != i
            ):
                ans = len(s)
        return ans


# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findLUSlength(strs)
    print("\noutput:", serialize(ans, "integer"))
