# Created by shiyang07ca at 2023/11/06 10:41
# leetgo: dev
# https://leetcode.cn/problems/maximum-product-of-word-lengths/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        cnt = [None] * n
        for i, w in enumerate(words):
            cnt[i] = {"len": len(w), "set": set(w)}

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                new_ans = cnt[i]["len"] * cnt[j]["len"]
                if (
                    len(cnt[i]["set"].intersection(cnt[j]["set"])) == 0
                    and new_ans > ans
                ):
                    ans = new_ans

        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxProduct(words)

    print("\noutput:", serialize(ans))
