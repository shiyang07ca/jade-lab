"""

Fenwick Tree / Binary Indexed Tree


"""


class BIT:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.c = [0] * (self.n + 1)

    def build(self):
        for i in range(self.n):
            self.update(i, self.arr[i])

    def lowbit(self, i):
        return i & (-i)

    def update(self, i, val):  # update index i
        i += 1
        while i <= self.n:
            # print(i)
            self.c[i] += val
            i += self.lowbit(i)

    def query(self, i):  # query cumulative from index 0 to i
        ans = 0
        i += 1
        while i > 0:
            ans += self.c[i]
            i -= self.lowbit(i)
        return ans


import unittest


class TestBIT(unittest.TestCase):
    def test_construct_tree_with_update_1(self):
        arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        bit_tree = BIT(arr)
        bit_tree.build()
        self.assertEqual(12, bit_tree.query(5))

        arr[3] += 6
        bit_tree.update(3, 6)
        self.assertEqual(18, bit_tree.query(5))

    def test_construct_tree_with_update_2(self):
        arr = [1, 2, 3, 4, 5]
        bit_tree = BIT(arr)
        bit_tree.build()
        self.assertEqual(10, bit_tree.query(3))

        arr[3] -= 5
        bit_tree.update(3, -5)
        self.assertEqual(5, bit_tree.query(3))

    def test_construct_tree_with_update_3(self):
        arr = [2, 1, 4, 6, -1, 5, -32, 0, 1]
        bit_tree = BIT(arr)
        bit_tree.build()
        self.assertEqual(12, bit_tree.query(4))

        arr[2] += 11
        bit_tree.update(2, 11)
        self.assertEqual(23, bit_tree.query(4))


if __name__ == "__main__":
    unittest.main()
