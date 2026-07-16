# Created by shiyang07ca at 2024/03/07 13:20
# leetgo: dev
# https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/solutions/2134227/cong-zuo-dao-you-ji-suan-by-endlesscheng-ywls/
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        x = 0
        for d in map(int, word):
            x = (x * 10 + d) % m
            ans.append(0 if x else 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().divisibilityArray(word, m)

    print("\noutput:", serialize(ans))
