# Created by shiyang07ca at 2024/01/05 00:22
# leetgo: dev
# https://leetcode.cn/problems/number-of-visible-people-in-a-queue/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Monotonic Stack


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-visible-people-in-a-queue/solutions/2591558/dan-diao-zhan-de-ben-zhi-ji-shi-qu-diao-8tp3s/
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and st[-1] < heights[i]:
                st.pop()
                ans[i] += 1
            if st:  # 还可以再看到一个人
                ans[i] += 1
            st.append(heights[i])
        return ans


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canSeePersonsCount(heights)

    print("\noutput:", serialize(ans))
