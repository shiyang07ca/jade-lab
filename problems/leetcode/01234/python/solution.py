# Created by shiyang07ca at 2023/07/12 21:00
# leetgo: dev
# https://leetcode.cn/problems/replace-the-substring-for-balanced-string/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: Sliding Window

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/replace-the-substring-for-balanced-string/solution/tong-xiang-shuang-zhi-zhen-hua-dong-chua-z7tu/


根据题意，如果在待替换子串之外的任意字符的出现次数都超过 m= n / 4 ，那么无论怎么
替换，都无法使这个字符的出现次数等于 m。

反过来说，如果在待替换子串之外的任意字符的出现次数都不超过m，那么可以通过替换，
使 s 为平衡字符串，即每个字符的出现次数均为 m。

这可以用同向双指针（长度不固定的滑动窗口）实现，对于本题，设子串的左右端点为
left 和 right，枚举 right，如果子串外的任意字符的出现次数都不超过 m，则说明从
left 到 right 的这段子串可以是待替换子串，用其长度 right − left + 1 更新答案的最
小值，并向右移动 left，缩小子串长度。



相似题目

LC3. 无重复字符的最长子串 https://leetcode.cn/problems/longest-substring-without-repeating-characters/

LC209. 长度最小的子数组 https://leetcode.cn/problems/minimum-size-subarray-sum/

LC713. 乘积小于 K 的子数组 https://leetcode.cn/problems/subarray-product-less-than-k/


"""


class Solution:
    def balancedString(self, s: str) -> int:
        cnt, m = Counter(s), len(s) // 4
        if all(cnt[x] == m for x in "QWER"):  # 已经符合要求啦
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1
            while all(cnt[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().balancedString(s)

    print("\noutput:", serialize(ans))
