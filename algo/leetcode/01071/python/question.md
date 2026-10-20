# [1071. 字符串的最大公因子][link] (Easy)

[link]: https://leetcode.cn/problems/greatest-common-divisor-of-strings/

对于字符串 `s` 和 `t`，只有当 `s` 由 `t` 重复连接一次或多次组成时，才认为 `t` 能除尽 `s`。

给定两个字符串 `str1` 和 `str2`，返回最长字符串 `x`，使得 `x` 能除尽 `str1` 且能除尽 `str2`。

**示例 1：**

**输入：** str1 = "ABCABC", str2 = "ABC"

**输出：**"ABC"

**示例 2：**

**输入：** str1 = "ABABAB", str2 = "ABAB"

**输出：**"AB"

**示例 3：**

**输入：** str1 = "LEET", str2 = "CODE"

**输出：**""

**示例 4：**

**输入：** str1 = "AAAAAB", str2 = "AAA"

**输出：**""

**提示：**

- `1 <= str1.length, str2.length <= 1000`
- `str1` 和 `str2` 由大写英文字母组成
