r"""















"""


def manacher_len(s):
    if len(s) < 2:
        return len(s)

    n_str = "#" + "#".join(s) + "#"
    print(f"nstr: {s} {n_str}")

    # 回文半径数组
    p_arr = [0] * len(n_str)
    # 回文最右坐标 + 1
    p_r = -1
    # 回文中心坐标
    index = -1
    ans = -1
    print(p_arr)

    for i in range(len(n_str)):
        p_arr[i] = min(p_arr[2 * index - i], p_r - i) if p_r > i else 1

        # 开始扩的过程
        while i + p_arr[i] < len(n_str) and i - p_arr[i] > -1:
            print(p_arr, i, p_arr[i], i + p_arr[i], i - p_arr[i])
            if n_str[i + p_arr[i]] == n_str[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break

        # 更新回文最右坐标以及中心坐标
        if i + p_arr[i] > p_r:
            p_r = i + p_arr[i]
            index = i
        ans = max(ans, p_arr[i])

    return ans - 1


def manacher_substr(s):
    if len(s) < 2:
        return s

    n_str = "#" + "#".join(s) + "#"
    print(f"nstr: {s} {n_str}")

    # 回文半径数组
    p_arr = [0] * len(n_str)
    # 回文最右坐标 + 1
    p_r = -1
    # 回文中心坐标
    index = -1
    max_len = -1
    print(p_arr)
    # 最长回文串起始坐标
    start = 0

    for i in range(len(n_str)):
        p_arr[i] = min(p_arr[2 * index - i], p_r - i) if p_r > i else 1

        # 开始扩的过程
        while i + p_arr[i] < len(n_str) and i - p_arr[i] > -1:
            # print(p_arr, i, p_arr[i], i + p_arr[i], i - p_arr[i])
            if n_str[i + p_arr[i]] == n_str[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break

        # 更新回文最右坐标以及中心坐标
        if i + p_arr[i] > p_r:
            p_r = i + p_arr[i]
            index = i

        if max_len < p_arr[i]:
            max_len = p_arr[i]
            start = i
        # print(f'max: {max_len}, start: {start}')

    ans = ""
    sub_str = n_str[start - max_len + 1 : start + max_len - 1]
    # print('sub_str ', sub_str)
    for c in sub_str:
        if c != "#":
            ans += c

    # print('ans ', ans)
    return ans


def short_add_substr(s):
    if len(s) < 2:
        return s

    n_str = "#" + "#".join(s) + "#"
    print(f"nstr: {s} {n_str}")

    # 回文半径数组
    p_arr = [0] * len(n_str)
    # 回文最右坐标 + 1
    p_r = -1
    # 回文中心坐标
    index = -1
    print(p_arr)
    ans = ""

    for i in range(len(n_str)):
        p_arr[i] = min(p_arr[2 * index - i], p_r - i) if p_r > i else 1

        # 开始扩的过程
        while i + p_arr[i] < len(n_str) and i - p_arr[i] > -1:
            # print(p_arr, i, p_arr[i], i + p_arr[i], i - p_arr[i])
            if n_str[i + p_arr[i]] == n_str[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break

        # 更新回文最右坐标以及中心坐标
        if i + p_arr[i] > p_r:
            p_r = i + p_arr[i]
            index = i

        # 当前回文最右坐标已经到达字符串末尾
        print(p_arr, i, p_arr[i], p_r - p_arr[i] * 2 + 1)
        if p_r == len(n_str):
            sub_str = n_str[0 : p_r - p_arr[i] * 2 + 1]
            print(f"sub: ==={sub_str}===")

            for c in sub_str[::-1]:
                if c != "#":
                    ans += c

            print("ans ", ans)
            return ans


def longest_palindrome_length(s):
    return manacher_len(s)


def longest_palindrome(s):
    return manacher_substr(s)


import unittest


class TestLongestPalindromicLength(unittest.TestCase):
    """最长回文子串长度"""

    def test_longest_palindromic_substring(self):
        self.assertEqual(len("bb"), longest_palindrome_length("cbbd"))
        self.assertEqual(len("abba"), longest_palindrome_length("abba"))
        self.assertEqual(
            len("asdadsa"), longest_palindrome_length("dasdasdasdasdasdadsa")
        )
        self.assertEqual(len("abba"), longest_palindrome_length("cabba"))
        self.assertEqual(len("abba"), longest_palindrome_length("cabba"))


class TestLongestPalindromicSubstring(unittest.TestCase):
    """最长回文子串"""

    def test_longest_palindromic_substring(self):
        self.assertEqual("bb", longest_palindrome("cbbd"))
        self.assertEqual("abba", longest_palindrome("abba"))
        self.assertEqual("asdadsa", longest_palindrome("dasdasdasdasdasdadsa"))
        self.assertEqual("abba", longest_palindrome("cabba"))
        self.assertEqual("abcba", longest_palindrome("cabcba"))


class TestPalindromicShortAdd(unittest.TestCase):
    """在字符串的最后添加最少字符，使整个字符串都成为回文串"""

    def test_longest_palindromic_substring(self):
        self.assertEqual("", short_add_substr("abba"))
        self.assertEqual("c", short_add_substr("cabba"))
        self.assertEqual("bbc", short_add_substr("cbbd"))
        self.assertEqual("dcba", short_add_substr("abcd123321"))
        self.assertEqual("c", short_add_substr("cabcba"))


def main():
    pass


if __name__ == "__main__":
    main()
