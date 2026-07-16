# Created by shiyang07ca at 2023/05/19 21:05
# https://leetcode.cn/problems/letter-tile-possibilities/

"""
1079. 活字印刷 (Medium)
你有一套活字字模 `tiles`，其中每个字模上都刻有一个字母 `tiles[i]`。返回你可以印出的非空字母序列的数
目。

**注意：** 本题中，每个活字字模只能使用一次。

**示例 1：**

```
输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

```

**示例 2：**

```
输入："AAABBC"
输出：188

```

**示例 3：**

```
输入："V"
输出：1
```

**提示：**

- `1 <= tiles.length <= 7`
- `tiles` 由大写英文字母组成

"""
from math import comb

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: dp
# TODO:


class Solution:
    def numTilePossibilities1(self, tiles: str) -> int:
        cnt = set()

        def dfs(c):
            t = set()
            nonlocal cnt
            for s in cnt:
                for j in range(len(s) + 1):
                    t.add(s[:j] + c + s[j:])
            cnt.add(c)
            cnt = cnt.union(t)

        for c in tiles:
            dfs(c)
        return len(cnt)

    # 链接：https://leetcode.cn/problems/letter-tile-possibilities/solutions/2275356/on2-ji-shu-dppythonjavacgo-by-endlessche-hmez/
    # 定义 f[i][j] 表示用前 i 种字符构造长为 j 的序列的方案数
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles).values()  # 统计每个字母的出现次数
        n, m = len(tiles), len(counts)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1  # 构造空序列的方案数
        for i, cnt in enumerate(counts, 1):  # 枚举第 i 种字母
            for j in range(n + 1):  # 枚举序列长度 j
                for k in range(min(j, cnt) + 1):  # 枚举第 i 种字母选了 k 个
                    f[i][j] += f[i - 1][j - k] * comb(j, k)  # comb 也可以预处理，见其它语言
        return sum(f[m][1:])


# @lc code=end

if __name__ == "__main__":
    tiles: str = deserialize("str", read_line())
    ans = Solution().numTilePossibilities(tiles)

    print("\noutput:", serialize(ans))
