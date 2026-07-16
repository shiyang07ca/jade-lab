# Created by shiyang07ca at 2023/04/29 11:20
# https://leetcode.cn/problems/remove-letter-to-equalize-frequency/

"""
2423. 删除字符使频率相同 (Easy)
给你一个下标从 **0** 开始的字符串 `word` ，字符串只包含小写
英文字母。你需要选择 **一个** 下标并 **删除** 下标处的字符，
使得 `word` 中剩余每个字母出现 **频率** 相同。

如果删除一个字母后， `word` 中剩余所有字母的出现频率都相同，
那么返回 `true` ，否则返回 `false` 。

**注意：**

- 字母 `x` 的 **频率** 是这个字母在字符串中出现的次数。
- 你 **必须** 恰好删除一个字母，不能一个字母都不删除。

**示例 1：**

```
输入：word = "abcc"
输出：true
解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出
现频率都为 1 。

```

**示例 2：**

```
输入：word = "aazz"
输出：false
解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z"
的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字
母出现频率相同。

```

**提示：**

- `2 <= word.length <= 100`
- `word` 只包含小写英文字母。

"""

from typing import *
from leetgo_py import *

from collections import *

# @lc code=begin


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/remove-letter-to-equalize-frequency/solutions/2249734/liang-chong-fang-fa-bao-li-fen-lei-tao-l-crt9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):  # 枚举删除的字符
            cnt = Counter(word[:i] + word[i + 1 :])  # 统计出现次数
            if len(set(cnt.values())) == 1:  # 出现次数都一样
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().equalFrequency(word)
    print("output:", serialize(ans))
