# Created by shiyang07ca at 2026/10/04 15:06
# leetgo: 1.4.17
# https://leetcode.cn/problems/maximum-subsequence-score/

from heapq import heappop, heappush
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(
            zip(nums1, nums2, strict=True),
            key=lambda pair: pair[1],
            reverse=True,
        )
        heap = []
        selected_sum = 0
        best_score = 0

        for value, min_value in pairs:
            # 堆中原本保留之前最大的 k - 1 个 nums1 值
            heappush(heap, value)
            selected_sum += value

            if len(heap) == k:
                # 当前元素必选， 因此当前 nums2 就是所选元素最小值
                best_score = max(best_score, selected_sum * min_value)

                # 为下一轮保留最大的 k - 1 个值
                selected_sum -= heappop(heap)

        return best_score


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
