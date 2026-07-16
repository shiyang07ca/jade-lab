# Created by shiyang07ca at 2023/11/23 13:35
# leetgo: dev
# https://leetcode.cn/problems/html-entity-parser/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def entityParser(self, text: str) -> str:
        for a, b in [
            ("&quot;", '"'),
            ("&apos;", "'"),
            ("&gt;", ">"),
            ("&lt;", "<"),
            ("&frasl;", "/"),
            ("&amp;", "&"),
        ]:
            text = text.replace(a, b)

        return text


# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().entityParser(text)

    print("\noutput:", serialize(ans))
