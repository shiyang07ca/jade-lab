"""

Binary Search

LC34. 在排序数组中查找元素的第一个和最后一个位置 https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

LC2560/WC331. 打家劫舍 IV https://leetcode.cn/problems/house-robber-iv/


"""

import unittest


# 左闭右闭 [l, r]
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return None


# 左闭右开 [l, r)
def binary_search2(arr, target):
    l, r = 0, len(arr)
    while l < r:
        # [l, r]  mid
        # [2, 3]   2
        # [2, 4]   3
        # [2, 5]   3
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid

    return None


"""

target = 3

      < target     <= target
        的上界       的上界
        |           |
        v           V
0   1   2   3   3   3   4   5   6
            |           |
     >= target的下界      > target 的下界
    C++: lower_bound   C++: upper_bound
    Python:bisect_left Python: bisect_right

>= bisect_left :  在有序数组中查询大于或等于某个数的最小数
>  bisect_right:  在有序数组中查询大于某个数的最小数

<=             :  在有序数组中查询小于或等于某个数的最大数
   bisect_right - 1

<              :  在有序数组中查询小于某个数的最大数
   bisect_left - 1

"""


# 查找左边界
# 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
def bs3(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) >> 1
        if arr[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l


# 查找右边界
# 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
def bs4(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r + 1) >> 1
        if arr[mid] <= target:
            l = mid
        else:
            r = mid - 1

    return l


def binary_search_recur(array, low, high, val):
    """
    Worst-case Complexity: O(log(n))

    reference: https://en.wikipedia.org/wiki/Binary_search_algorithm
    """

    if low > high:  # error case
        return -1
    mid = (low + high) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    return mid


class TestSuite(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, binary_search(array, 5))
        self.assertEqual(11, binary_search(array, 6))
        self.assertEqual(None, binary_search(array, 7))
        self.assertEqual(None, binary_search(array, -1))

        self.assertEqual(10, binary_search2(array, 5))
        self.assertEqual(11, binary_search2(array, 6))
        self.assertEqual(None, binary_search2(array, 7))
        self.assertEqual(None, binary_search2(array, -1))

        # Test binary_search_recur
        self.assertEqual(10, binary_search_recur(array, 0, 11, 5))
        self.assertEqual(11, binary_search_recur(array, 0, 11, 6))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, 7))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, -1))

    def test_2(self):
        from bisect import bisect_left, bisect_right

        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        # self.assertEqual(10, bs3(array, 5))
        # self.assertEqual(11, bs3(array, 6))

        #      0  1  2  3  4  5  6  7  8
        arr = [0, 1, 2, 3, 3, 3, 4, 5, 6]
        self.assertEqual(3, bs3(arr, 3))
        self.assertEqual(bisect_left(arr, 3), bs3(arr, 3))  # 3, 3
        self.assertEqual(5, bs4(arr, 3))

        print(bs3(arr, 7), bisect_left(arr, 7))  # 8  9
        print(bs3(arr, -1), bisect_left(arr, -1))  # 0  0

        print("################################################################")

        # arr = [0, 1, 2, 3, 4, 5, 6]
        arr = [0]
        print(bs3(arr, 5), bisect_left(arr, 5))  # 0  1
        print(bs3(arr, -1), bisect_left(arr, -1))  # 0  0

        print(bs4(arr, 5), bisect_right(arr, 5))  # 0  1
        print(bs4(arr, -1), bisect_right(arr, -1))  # 0  0


if __name__ == "__main__":

    unittest.main()
