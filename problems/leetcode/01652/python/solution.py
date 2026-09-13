from __future__ import annotations

# Created by shiyang07ca at 2024/05/05 00:09
# leetgo: dev
# https://leetcode.cn/problems/defuse-the-bomb/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        ans = []
        n = len(code)
        f = 0
        if k > 0:
            f = 1
        elif k < 0:
            f = -1
        for i, c in enumerate(code):
            t = 0
            if f != 0:
                for j in range(i + f, i + f + k, f):
                    t += code[j % n]
            ans.append(t)

        return ans


# @lc code=end

if __name__ == "__main__":
    code: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decrypt(code, k)
    print("\noutput:", serialize(ans, "integer[]"))
