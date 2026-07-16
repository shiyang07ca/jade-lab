# Created by shiyang07ca at 2024/04/18 23:01
# leetgo: dev
# https://leetcode.cn/problems/find-original-array-from-doubled-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-original-array-from-doubled-array/solutions/2744966/san-chong-fang-fa-cong-onlogn-dao-onpyth-irrt/
    def findOriginalArray1(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        cnt = Counter()
        for x in changed:
            if x not in cnt:  # x 不是双倍后的元素
                cnt[x * 2] += 1  # 标记一个双倍元素
                ans.append(x)
            else:  # x 是双倍后的元素
                cnt[x] -= 1  # 清除一个标记
                if cnt[x] == 0:
                    del cnt[x]
        # 只有所有双倍标记都被清除掉，才能说明 changed 是一个双倍数组
        return [] if cnt else ans

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        q = deque()
        for x in changed:
            if q:
                if q[0] < x:  # 无法配对
                    return []
                if q[0] == x:  # 配对成功
                    q.popleft()  # 清除一个标记
                    continue
            ans.append(x)
            q.append(x * 2)  # 添加双倍标记
        # 只有所有双倍标记都被清除掉，才能说明 changed 是一个双倍数组
        return [] if q else ans


# @lc code=end

if __name__ == "__main__":
    changed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findOriginalArray(changed)
    print("\noutput:", serialize(ans, "integer[]"))
