# Created by shiyang07ca at 2023/11/27 00:01
# leetgo: dev
# https://leetcode.cn/problems/sum-of-subarray-minimums/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# template
# tag: Monotone Stack


"""

https://leetcode.cn/problems/sum-of-subarray-minimums/solution/gong-xian-fa-dan-diao-zhan-san-chong-shi-gxa5/

思路

找到以每个元素为最小值的子树组个数，也就是找到比当前元素的小的左右边界，
计算子树组个数，乘以当前元素，就是对总和的贡献


i      0       1        2        3    4
a    [ 3       1        2        4 ]

    (-1, 1)   (-1, 4)  (1, 4)   (2, 4)

     1 * 1      2 * 3    1 * 2     1 * 1
     3 * 1 +   1 * 6  +  2 * 2 +  4 * 1  = 17

"""


class Solution:
    def sumSubarrayMins1(self, arr: List[int]) -> int:
        pos = [[]] * len(arr)
        st = []
        N = len(arr)

        for i, n in enumerate(arr):
            while st and arr[st[-1]] >= n:
                index = st.pop()
                left = st[-1] if st else -1
                pos[index] = [left, i]
            st.append(i)

        while st:
            index = st.pop()
            left = st[-1] if st else -1
            pos[index] = [left, N]

        print(f"pos: {pos}")

        ans = 0
        MOD = 10**9 + 7
        for i, (l, r) in enumerate(pos):
            ans += (i - l) * (r - i) * arr[i]

        return ans % MOD

    def sumSubarrayMins(self, arr: List[int]) -> int:
        def get_near_more(nums):
            N = len(nums)
            left = [-1] * N  # left[i] 为左侧严格小于等于 nums[i] 的最近元素位置（不存在时为-1）
            right = [N] * N  # right[i] 为右侧严格小于 nums[i] 的最近元素位置（不存在时为 N）
            st = []
            for i, n in enumerate(nums):
                while st and nums[st[-1]] > n:
                    popi = st.pop()
                    right[popi] = i
                left[i] = st[-1] if st else -1
                st.append(i)

            return [[l, r] for l, r in zip(left, right)]

        ans = 0
        MOD = 10**9 + 7
        stk = get_near_more(arr)

        for (i, n), (l, r) in zip(enumerate(arr), stk):
            print(n, l, i, r, ans)
            ans += n * (i - l) * (r - i)

        return ans % MOD


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumSubarrayMins(arr)

    print("\noutput:", serialize(ans))
