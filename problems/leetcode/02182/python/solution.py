# Created by shiyang07ca at 2024/01/13 13:37
# leetgo: dev
# https://leetcode.cn/problems/construct-string-with-repeat-limit/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        ans = []
        i = 25
        while True:
            if i == -1:
                return "".join(ans)

            if cnt[i] > limit:
                cnt[i] -= limit
                ans += [chr(ord("a") + i)] * limit
                for j in range(i - 1, -2, -1):
                    if j == -1:
                        return "".join(ans)

                    if cnt[j] >= 1:
                        cnt[j] -= 1
                        ans.append(chr(ord("a") + j))
                        break
            else:
                ans += [chr(ord("a") + i)] * cnt[i]
                cnt[i] = 0
                i -= 1


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    repeatLimit: int = deserialize("int", read_line())
    ans = Solution().repeatLimitedString(s, repeatLimit)

    print("\noutput:", serialize(ans))
