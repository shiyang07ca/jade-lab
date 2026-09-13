from __future__ import annotations

# Created by shiyang07ca at 2023/08/13 00:35
# leetgo: dev
# https://leetcode.cn/problems/merge-sorted-array/
from typing import cast

# leetgo_py does not ship type stubs.
# pyright: reportMissingTypeStubs=false
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def merge1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        cur = m + n - 1
        while cur >= 0 and m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[cur] = nums1[m - 1]
                m -= 1
            else:
                nums1[cur] = nums2[n - 1]
                n -= 1
            cur -= 1
        while (cur >= 0 and m > 0) or n > 0:
            if m > 0:
                nums1[cur] = nums1[m - 1]
                m -= 1
            elif n > 0:
                nums1[cur] = nums2[n - 1]
                n -= 1
            cur -= 1

    # https://leetcode.cn/problems/merge-sorted-array/solutions/126371/88-by-ikaruga/
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        m, n = m - 1, n - 1
        while n >= 0:
            while m >= 0 and nums1[m] > nums2[n]:
                nums1[i], nums1[m] = nums1[m], nums1[i]
                i -= 1
                m -= 1
            nums1[i], nums2[n] = nums2[n], nums1[i]
            i -= 1
            n -= 1


# @lc code=end

if __name__ == "__main__":
    nums1 = cast(list[int], deserialize("List[int]", read_line()))
    m = cast(int, deserialize("int", read_line()))
    nums2 = cast(list[int], deserialize("List[int]", read_line()))
    n = cast(int, deserialize("int", read_line()))
    Solution().merge(nums1, m, nums2, n)
    ans = nums1

    print("\noutput:", serialize(ans))
