# Created by shiyang07ca at 2023/09/28 17:35
# leetgo: dev
# https://leetcode.cn/problems/number-of-flowers-in-full-bloom/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: binary search, 差分数组

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-flowers-in-full-bloom/description/
    def fullBloomFlowers1(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]

    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        diff = Counter()
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted(diff.keys())

        j = s = 0
        for p, i in sorted(zip(people, range(len(people)))):
            while j < len(times) and times[j] <= p:
                s += diff[times[j]]  # 累加不超过 people[i] 的差分值
                j += 1
            people[i] = s  # 从而得到这个时刻花的数量
        return people


# @lc code=end

if __name__ == "__main__":
    flowers: List[List[int]] = deserialize("List[List[int]]", read_line())
    people: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fullBloomFlowers(flowers, people)

    print("\noutput:", serialize(ans))
