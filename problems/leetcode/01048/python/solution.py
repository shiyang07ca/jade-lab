# Created by shiyang07ca at 2023/04/27 22:51
# https://leetcode.cn/problems/longest-string-chain/

"""
1048. 最长字符串链 (Medium)
给出一个单词数组 `words` ，其中每个单词都由小写英文字母组成
。

如果我们可以 **不改变其他字符的顺序**，在 `wordA` 的任何地方
添加 **恰好一个** 字母使其变成 `wordB` ，那么我们认为 `wordA
` 是 `wordB` 的 **前身** 。

- 例如， `"abc"` 是 `"abac"` 的 **前身** ，而 `"cba"` 不是 `
"bcad"` 的 **前身**

**词链** 是单词 `[word_1, word_2, ..., word_k]` 组成的序列，
`k >= 1`，其中 `word₁` 是 `word₂` 的前身， `word₂` 是 `word₃
` 的前身，依此类推。一个单词通常是 `k == 1` 的 **单词链** 。

从给定单词列表 `words` 中选择单词组成词链，返回 词链的 **最
长可能长度** 。

**示例 1：**

```
输入：words = ["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 ["a","ba","bda","bdca"]

```

**示例 2:**

```
输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
输出：5
解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxb
c", "pcxbcf"].

```

**示例 3:**

```
输入：words = ["abcd","dbqca"]
输出：1
解释：字链["abcd"]是最长的字链之一。
["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变
了。

```

**提示：**

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 16`
- `words[i]` 仅由小写英文字母组成。

"""

from typing import *
from leetgo_py import *
from functools import *

# @lc code=begin


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ws = sorted([(len(w), w) for w in words], reverse=True)
        wpos = {w[1]: i for i, w in enumerate(ws)}

        @cache
        def dfs(i):
            ans = 1
            if i >= len(ws):
                return 0
            w = ws[i][1]
            for j in range(len(w)):
                nw = w[:j] + w[j + 1 :]
                if nw not in wpos:
                    continue
                ans = max(dfs(wpos[nw]) + 1, ans)
            return ans

        return max([dfs(i) for i in range(len(ws))])

    # 作者：灵茶山艾府
    # 链接：https://leetcode.cn/problems/longest-string-chain/solutions/2247269/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-wdkm/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def longestStrChain(self, words: List[str]) -> int:
        ws = set(words)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(s: str) -> int:
            res = 0
            for i in range(len(s)):  # 枚举去掉 s[i]
                t = s[:i] + s[i + 1 :]
                if t in ws:  # t 在 words 中
                    res = max(res, dfs(t))
            return res + 1

        return max(dfs(s) for s in ws)


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestStrChain(words)
    print("output:", serialize(ans))
