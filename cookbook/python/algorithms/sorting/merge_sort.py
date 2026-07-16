"""

归并排序


"""


# 朴素指针做法
def merge_sort(a, l, r):
    if l >= r:
        return

    mid = (l + r) >> 1

    merge_sort(a, l, mid)
    merge_sort(a, mid + 1, r)

    i, j = l, mid + 1
    tmp = []
    while i <= mid and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= mid:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1

    k = 0
    for i in range(l, r + 1):
        a[i] = tmp[k]
        k += 1


def merge_sort2(a):
    def _merge(left, right, merged):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged[l + r] = left[l]
                l += 1
            else:
                merged[l + r] = right[r]
                r += 1
        for l in range(l, len(left)):
            merged[l + r] = left[l]
        for r in range(r, len(right)):
            merged[l + r] = right[r]

        return merged

    N = len(a)
    if N <= 1:
        return a

    mid = N // 2
    left, right = merge_sort2(a[:mid]), merge_sort2(a[mid:])

    _merge(left, right, a)
    return a


def is_sorted(array):
    """
    Helper function to check if the given array is sorted.
    :param array: Array to check if sorted
    :return: True if sorted in ascending order, else False
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        """"""

    def test_s(self):
        nums = [1, 3, 2, 5, 65, 23, 57, 1232]
        merge_sort(nums, 0, len(nums) - 1)
        print(nums)
        self.assertTrue(is_sorted(nums))

        nums2 = [4, 3, 2, 5, 65, 23, 57]
        merge_sort(nums2, 0, len(nums2) - 1)
        print(nums2)
        self.assertTrue(is_sorted(nums2))

    def test_s2(self):
        nums = [1, 3, 2, 5, 65, 23, 57, 1232]
        nums2 = merge_sort2(nums)
        print(nums)
        self.assertTrue(is_sorted(nums))
        self.assertTrue(is_sorted(nums2))


if __name__ == "__main__":
    unittest.main()
