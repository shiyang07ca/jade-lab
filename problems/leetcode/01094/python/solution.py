# Created by shiyang07ca at 2023/10/06 10:58
# leetgo: dev
# https://leetcode.cn/problems/car-pooling/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: 差分数组


class Solution:
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        n = 1001
        diff = [0] * n
        for x, left, right in trips:
            diff[left] += x
            diff[right] -= x

        for i in range(1, n):
            diff[i] += diff[i - 1]

        for d in diff:
            if d > capacity:
                return False

        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0] * 1001
        for num, from_, to in trips:
            d[from_] += num
            d[to] -= num
        return all(s <= capacity for s in accumulate(d))

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = Counter()
        for num, from_, to in trips:
            d[from_] += num
            d[to] -= num
        s = 0
        for k in sorted(d):
            s += d[k]
            if s > capacity:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().carPooling(trips, capacity)

    print("\noutput:", serialize(ans))
