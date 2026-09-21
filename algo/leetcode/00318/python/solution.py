from __future__ import annotations

# Created by shiyang07ca at 2023/11/06 10:41
# leetgo: dev
# https://leetcode.cn/problems/maximum-product-of-word-lengths/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        cnt: list[tuple[int, set[str]]] = [(0, set()) for _ in range(n)]
        for i, w in enumerate(words):
            cnt[i] = len(w), set(w)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                new_ans = cnt[i][0] * cnt[j][0]
                if (
                    len(cnt[i][1].intersection(cnt[j][1])) == 0
                    and new_ans > ans
                ):
                    ans = new_ans

        return ans


# @lc code=end

if __name__ == "__main__":
    words: list[str] = deserialize("List[str]", read_line())
    ans = Solution().maxProduct(words)

    print("\noutput:", serialize(ans))
