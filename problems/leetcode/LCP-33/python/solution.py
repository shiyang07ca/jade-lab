# Created by shiyang07ca at 2023/05/21 00:33
# https://leetcode.cn/problems/o8SXZn/

"""
LCP 33. 蓄水 (Easy)
给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 \`i\` 个水缸配备的水桶容量记作 \
`bucket\[i\]\`。小扣有以下两种操作：
\- 升级水桶：选择任意一个水桶，使其容量增加为 \`bucket\[i\]+1\`
\- 蓄水：将全部水桶接满水，倒入各自对应的水缸

每个水缸对应最低蓄水量记作 \`vat\[i\]\`，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

注意：实际蓄水量 \\*\\*达到或超过\\*\\* 最低蓄水量，即完成蓄水要求。

\*\*示例 1：\*\*
>输入：\`bucket = \[1,3\], vat = \[6,8\]\`
>
>输出：\`4\`
>
>解释：
>第 1 次操作升级 bucket\[0\]；
>第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。
!\[vat1.gif\](https://pic.leetcode-cn.com/1616122992-RkDxoL-vat1.gif)

\*\*示例 2：\*\*
>输入：\`bucket = \[9,0,1\], vat = \[0,2,2\]\`
>
>输出：\`3\`
>
>解释：
>第 1 次操作均选择升级 bucket\[1\]
>第 2~3 次操作选择蓄水，即可完成蓄水要求。

\\*\\*提示：\\*\\*
\- \`1 <= bucket.length == vat.length <= 100\`
\- \`0 <= bucket\[i\], vat\[i\] <= 10^4\`

"""
from heapq import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: greedy


# 链接：https://leetcode.cn/problems/o8SXZn/solutions/2277623/python3javacgotypescript-yi-ti-yi-jie-ta-awvh/
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        mx = max(vat)
        if mx == 0:
            return 0
        ans = inf
        for x in range(1, mx + 1):
            y = sum(max(0, (v + x - 1) // x - b) for v, b in zip(vat, bucket))
            ans = min(ans, x + y)
        return ans


# @lc code=end

if __name__ == "__main__":
    bucket: List[int] = deserialize("List[int]", read_line())
    vat: List[int] = deserialize("List[int]", read_line())
    ans = Solution().storeWater(bucket, vat)

    print("\noutput:", serialize(ans))
