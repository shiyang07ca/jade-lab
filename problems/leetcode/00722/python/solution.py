# Created by shiyang07ca at 2023/08/03 13:33
# leetgo: dev
# https://leetcode.cn/problems/remove-comments/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def removeComments1(self, source: List[str]) -> List[str]:
        # 匹配所有 // 和 /* */，后者用非贪婪模式。将所有匹配结果替换成空串。最后移除多余空行。
        return list(
            filter(
                None, re.sub("//.*|/\*(.|\n)*?\*/", "", "\n".join(source)).split("\n")
            )
        )

    # 链接：https://leetcode.cn/problems/remove-comments/solutions/2370636/python3javacgorust-yi-ti-yi-jie-fen-qing-0vka/
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        t = []
        block_comment = False
        for s in source:
            i, m = 0, len(s)
            while i < m:
                if block_comment:
                    if s[i : i + 2] == "*/":
                        block_comment = False
                        i += 1
                else:
                    if s[i : i + 2] == "/*":
                        block_comment = True
                        i += 1
                    elif s[i : i + 2] == "//":
                        break
                    else:
                        t.append(s[i])
                i += 1
            if not block_comment and t:
                ans.append("".join(t))
                t.clear()
        return ans


# @lc code=end

if __name__ == "__main__":
    source: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeComments(source)

    print("\noutput:", serialize(ans))
