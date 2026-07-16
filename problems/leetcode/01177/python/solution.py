# Created by shiyang07ca at 2023/06/15 00:00
# https://leetcode.cn/problems/can-make-palindrome-from-substring/

"""
1177. 构建回文串检测 (Medium)
给你一个字符串 `s`，请你对 `s` 的子串进行检测。

每次检测，待检子串都可以表示为 `queries[i] = [left, right, k]`。我们可以 **重新排列** 子串 `s[left],
..., s[right]`，并从中选择 **最多** `k` 项替换成任何小写英文字母。

如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 `true`，否则结果为 `false`。

返回答案数组 `answer[]`，其中 `answer[i]` 是第 `i` 个待检子串 `queries[i]` 的检测结果。

注意：在替换时，子串中的每个字母都必须作为 **独立的** 项进行计数，也就是说，如果 `s[left..right] = "
aaa"` 且 `k = 2`，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 `s`，可以认为每次
检测都是独立的）

**示例：**

```
输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把
"cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。

```

**提示：**

- `1 <= s.length, queries.length <= 10^5`
- `0 <= queries[i][0] <= queries[i][1] < s.length`
- `0 <= queries[i][2] <= s.length`
- `s` 中只有小写英文字母

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: prefix sum


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/can-make-palindrome-from-substring/solutions/2309725/yi-bu-bu-you-hua-cong-qian-zhui-he-dao-q-yh5p/
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord("a")] += 1

        ans = []
        for left, right, k in queries:
            m = 0
            for sl, sr in zip(sum[left], sum[right + 1]):
                m += (sr - sl) % 2  # 奇数+1，偶数+0
            ans.append(m // 2 <= k)
        return ans

    def canMakePaliQueries2(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord("a")] += 1
            sum[-1][ord(c) - ord("a")] %= 2  # 偶数是 0

        ans = []
        for left, right, k in queries:
            m = 0
            for sl, sr in zip(sum[left], sum[right + 1]):
                m += sr != sl
            ans.append(m // 2 <= k)
        return ans

    def canMakePaliQueries3(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord("a")] ^= 1  # 奇数变偶数，偶数变奇数

        ans = []
        for left, right, k in queries:
            m = 0
            for sl, sr in zip(sum[left], sum[right + 1]):
                m += sr ^ sl
            ans.append(m // 2 <= k)
        return ans

    def canMakePaliQueries4(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [0]
        for c in s:
            bit = 1 << (ord(c) - ord("a"))
            sum.append(sum[-1] ^ bit)  # 该比特对应字母的奇偶性：奇数变偶数，偶数变奇数

        ans = []
        for left, right, k in queries:
            m = (sum[left] ^ sum[right + 1]).bit_count()
            ans.append(m // 2 <= k)
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canMakePaliQueries(s, queries)

    print("\noutput:", serialize(ans))
