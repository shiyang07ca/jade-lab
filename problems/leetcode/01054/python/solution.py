# Created by shiyang07ca at 2023/05/14 09:34
# https://leetcode.cn/problems/distant-barcodes/

"""
1054. 距离相等的条形码 (Medium)
在一个仓库里，有一排条形码，其中第 `i` 个条形码为 `barcodes[
i]`。

请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。
你可以返回任何满足该要求的答案，此题保证存在答案。

**示例 1：**

```
输入：barcodes = [1,1,1,2,2,2]
输出：[2,1,2,1,2,1]

```

**示例 2：**

```
输入：barcodes = [1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
```

**提示：**

- `1 <= barcodes.length <= 10000`
- `1 <= barcodes[i] <= 10000`

"""
from itertools import *
from collections import *
from heapq import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rearrangeBarcodes1(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        ans = []
        h = [(-c, n) for n, c in cnt.items()]
        heapify(h)
        while len(ans) < len(barcodes):
            c1, n1 = heappop(h)
            if ans and ans[-1] == n1:
                c2, n2 = heappop(h)
                ans.append(n2)
                if c2 != -1:
                    heappush(h, (c2 + 1, n2))
            ans.append(n1)
            if c1 != -1:
                heappush(h, (c1 + 1, n1))

        return ans

    # 作者：ylb
    # 链接：https://leetcode.cn/problems/distant-barcodes/solutions/2268959/python3javacgotypescript-yi-ti-yi-jie-ji-3or2/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (-cnt[x], x))
        n = len(barcodes)
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[: (n + 1) // 2]
        ans[1::2] = barcodes[(n + 1) // 2 :]
        return ans


# @lc code=end

if __name__ == "__main__":
    barcodes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rearrangeBarcodes(barcodes)
    print("output:", serialize(ans))
