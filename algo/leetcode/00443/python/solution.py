# Created by shiyang07ca at 2026/10/02 14:19
# leetgo: 1.4.17
# https://leetcode.cn/problems/string-compression/

from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    """
    双指针

    设两个下标：

    - read：还没处理过的第一个字符的位置。
    - write：下一个输出字符应该放的位置。

    初始都是 0。处理一组时：

    1. 记住 ch = chars[read]，然后 read 向后扫，直到遇到不同字符或到数组末尾。这一组的长度 run 就得到了。
    2. 把 ch 写到 chars[write]，write += 1。
    3. 如果 run > 1，把 run 的十进制数字逐位写到 chars[write...]。
    """

    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0  # 下一个未处理的字符
        write = 0  # 下一个输出位置
        while read < n:
            ch = chars[read]
            run = 0
            while read < n and chars[read] == ch:
                read += 1
                run += 1
            chars[write] = ch
            write += 1
            if run > 1:
                for d in str(run):
                    chars[write] = d
                    write += 1
        return write


# @lc code=end

if __name__ == "__main__":
    chars: List[str] = deserialize("List[str]", read_line())
    ans = Solution().compress(chars)
    print("\noutput:", serialize(ans, "integer"))
