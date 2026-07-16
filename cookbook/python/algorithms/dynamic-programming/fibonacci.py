r"""

















"""

import unittest


def fib(n):
    pass


class Test(unittest.TestCase):
    def test(self):
        print("aaa")
        self.assertEqual(
            [1, 1, 2, 3, 5, 8, 13, 21],
            fib(8),
        )


if __name__ == "__main__":
    unittest.main()
