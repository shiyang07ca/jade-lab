from __future__ import annotations

# Created by shiyang07ca at 2023/09/02 09:27
# leetgo: dev
# https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured/solutions/2422340/python3javacgorust-yi-ti-yi-jie-shuang-z-xws6/
    def captureForts(self, forts: list[int]) -> int:
        n = len(forts)
        i = ans = 0
        while i < n:
            j = i + 1
            if forts[i]:
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[i] + forts[j] == 0:
                    ans = max(ans, j - i - 1)
            i = j
        return ans


# @lc code=end

if __name__ == "__main__":
    forts: list[int] = deserialize("List[int]", read_line())
    ans = Solution().captureForts(forts)

    print("\noutput:", serialize(ans))
