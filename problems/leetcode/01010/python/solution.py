# Created by shiyang07ca at 2023/05/07 01:16
# https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/

"""
1010. 总持续时间可被 60 整除的歌曲 (Medium)
在歌曲列表中，第 `i` 首歌曲的持续时间为 `time[i]` 秒。

返回其总持续时间（以秒为单位）可被 `60` 整除的歌曲对的数量。
形式上，我们希望下标数字 `i` 和 `j` 满足  `i < j` 且有 `(tim
e[i] + time[j]) % 60 == 0`。

**示例 1：**

```
输入：time = [30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整除：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60

```

**示例 2：**

```
输入：time = [60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整除。

```

**提示：**

- `1 <= time.length <= 6 * 10⁴`
- `1 <= time[i] <= 500`

"""
from collections import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2259343/liang-shu-zhi-he-de-ben-zhi-shi-shi-yao-bd0r1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        cnt = [0] * 60
        for t in time:
            # 先查询 cnt，再更新 cnt，因为题目要求 i<j
            # 如果先更新，再查询，就把 i=j 的情况也考虑进去了
            ans += cnt[(60 - t % 60) % 60]
            cnt[t % 60] += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numPairsDivisibleBy60(time)
    print("output:", serialize(ans))
