def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    p = arr.pop()
    greater = []
    lesser = []
    for e in arr:
        if e > p:
            greater.append(e)
        else:
            lesser.append(e)
    return quick_sort(lesser) + [p] + quick_sort(greater)


import random


def quick_sort2(arr):
    def partition(arr, lo, hi):
        pivot = arr[lo]
        print(f"lo: {lo}, pivot: {pivot}")
        i = lo + 1
        for j in range(lo + 1, hi):
            if arr[j] < pivot:
                print(j)
                arr[j], arr[i] = arr[i], arr[j]
                print(arr)
                i += 1
        arr[lo], arr[i - 1] = arr[i - 1], arr[lo]
        return i - 1

    def qs(arr, lo, hi):
        # print(lo, hi)
        if lo < hi:
            pivot = random.randint(lo, hi - 1)
            arr[pivot], arr[lo] = arr[lo], arr[pivot]
            pivot_index = partition(arr, lo, hi)
            qs(arr, lo, pivot_index)
            qs(arr, pivot_index + 1, hi)

    qs(arr, 0, len(arr))
    # print(arr)
    return arr


def quick_sort3(arr):
    def shuffle(arr):
        n = len(arr)
        for i in range(n):
            r = random.randint(i, n - 1)
            arr[r], arr[i] = arr[i], arr[r]

    def partition(arr, lo, hi):
        pivot = arr[lo]
        # [lo, i) <= pivot; (j, hi] > pivot
        i, j = lo + 1, hi
        while i <= j:
            # while 结束时 arr[i] > pivot
            while i < hi and arr[i] <= pivot:
                i += 1
            # while 结束时 arr[j] <= pivot
            while j > lo and arr[j] > pivot:
                j -= 1

            if i >= j:
                break

            # 此时 [lo, i) <= pivot and (j, hi] > pivot
            # 交换 arr[i], arr[i]
            # 此时 [lo, i] <= pivot and [j, hi] > pivot
            arr[j], arr[i] = arr[i], arr[j]

        arr[lo], arr[j] = arr[j], arr[lo]

        return j

    def qsort(arr, lo, hi):
        if lo >= hi:
            return

        # arr[lo..p-1] <= arr[p] < arr[p+1..hi]
        p = partition(arr, lo, hi)
        qsort(arr, lo, p - 1)
        qsort(arr, p + 1, hi)

    shuffle(arr)
    qsort(arr, 0, len(arr) - 1)
    return arr


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.s = quick_sort
        # self.s = quick_sort2
        self.s = quick_sort3
        # self.s = quick_sort_random

    def test1(self):
        self.assertEqual(self.s([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])
        print("################################################################")

        self.assertEqual(self.s([-2, 5, 0, -45]), [-45, -2, 0, 5])
        print("################################################################")

        self.assertEqual(self.s([]), [])


if __name__ == "__main__":
    unittest.main()
