# Created by shiyang07ca at 2024/01/09 00:17
# leetgo: dev
# https://leetcode.cn/problems/extra-characters-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/extra-characters-in-a-string/solutions/2286613/dong-tai-gui-hua-cong-ji-yi-hua-sou-suo-wtd7a/
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            res = dfs(i - 1) + 1  # 不选
            for j in range(i + 1):  # 枚举选哪个
                if s[j : i + 1] in d:
                    res = min(res, dfs(j - 1))
            return res

        return dfs(len(s) - 1)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    dictionary: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minExtraChar(s, dictionary)

    print("\noutput:", serialize(ans))
