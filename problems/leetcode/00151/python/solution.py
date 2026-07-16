# Created by shiyang07ca at 2025/02/04 14:01
# leetgo: 1.4.13
# https://leetcode.cn/problems/reverse-words-in-a-string/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseWords(self, s: str) -> str:
        # 链接：https://leetcode.cn/problems/reverse-words-in-a-string/solutions/2361551/151-fan-zhuan-zi-fu-chuan-zhong-de-dan-c-yb1r/
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1  # 搜索首个空格
            res.append(s[i + 1 : j + 1])  # 添加单词
            while i >= 0 and s[i] == " ":
                i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符
        return " ".join(res)  # 拼接并返回


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reverseWords(s)
    print("\noutput:", serialize(ans, "string"))
