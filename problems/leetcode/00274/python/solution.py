# Created by shiyang07ca at 2023/10/29 08:25
# leetgo: dev
# https://leetcode.cn/problems/h-index/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def hIndex1(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):
            if c < i:
                return i - 1
        return len(citations)

    # 链接：https://leetcode.cn/problems/h-index/solutions/2502896/gong-shui-san-xie-cong-po-ti-dao-zhu-bu-7sug6/
    def hIndex2(self, cs: List[int]) -> int:
        n = len(cs)
        l, r = 0, n
        while l < r:
            mid = (l + r + 1) // 2
            if sum(c >= mid for c in cs) >= mid:
                l = mid
            else:
                r = mid - 1
        return r

    # 链接：https://leetcode.cn/problems/h-index/solutions/2502896/gong-shui-san-xie-cong-po-ti-dao-zhu-bu-7sug6/
    def hIndex(self, cs: List[int]) -> int:
        n = len(cs)
        cnt = [0] * (n + 10)
        for c in cs:
            cnt[min(c, n)] += 1
        tot = 0
        for i in range(n, -1, -1):
            tot += cnt[i]
            if tot >= i:
                return i
        return -1  # never


# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)

    print("\noutput:", serialize(ans))
