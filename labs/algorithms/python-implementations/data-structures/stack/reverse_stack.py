"""

给你一个栈，请你逆序这个栈，不能申请额外的数据结构，
只能使用递归函数，如何实现？

"""

import unittest
from typing import List


class Solution:
    def f(self, stack):
        result = stack.pop()
        if not stack:
            return result
        else:
            last = self.f(stack)
            stack.append(result)
            return last

    def reverse(self, stack):
        if not stack:
            return

        last = self.f(stack)
        self.reverse(stack)
        stack.append(last)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 5, 2]
        self.sl.reverse(nums)
        self.assertEqual(tuple(nums), (2, 5, 1))

        nums = [1, 5, 233, 7]
        self.sl.reverse(nums)
        self.assertEqual(tuple(nums), (7, 233, 5, 1))


if __name__ == "__main__":
    unittest.main()
