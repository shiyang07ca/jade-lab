# Created by shiyang07ca at 2024/06/05 09:37
# leetgo: dev
# https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Fenwick:
    __slots__ = "tree"

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 1
    def add(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


class Solution:
    # 链接：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/solutions/2664646/chi-san-hua-shu-zhuang-shu-zu-pythonjava-3bb2/
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t1 = Fenwick(m + 1)
        t2 = Fenwick(m + 1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            gc1 = len(a) - t1.pre(v)  # greaterCount(a, v)
            gc2 = len(b) - t2.pre(v)  # greaterCount(b, v)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                t1.add(v)
            else:
                b.append(x)
                t2.add(v)
        return a + b


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().resultArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
