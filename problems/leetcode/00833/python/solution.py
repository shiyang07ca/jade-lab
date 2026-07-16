# Created by shiyang07ca at 2023/08/15 13:04
# leetgo: dev
# https://leetcode.cn/problems/find-and-replace-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/find-and-replace-in-string/solutions/2388853/xian-xing-zuo-fa-pythonjavacgojs-by-endl-uofo/
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        replace = [(c, 1) for c in s]
        for i, src, tar in zip(indices, sources, targets):
            if s.startswith(src, i):  # 判断 s[i:] 的前缀是否为 src，这样写无需切片
                replace[i] = (tar, len(src))  # (替换后的字符串，被替换的长度)

        ans = []
        i = 0
        while i < len(s):
            ans.append(replace[i][0])  # 替换后的字符串（默认为 s[i]）
            i += replace[i][1]  # 被替换的长度（默认为 1）
        return "".join(ans)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    indices: List[int] = deserialize("List[int]", read_line())
    sources: List[str] = deserialize("List[str]", read_line())
    targets: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findReplaceString(s, indices, sources, targets)

    print("\noutput:", serialize(ans))
