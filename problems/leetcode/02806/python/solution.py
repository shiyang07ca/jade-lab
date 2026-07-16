# Created by shiyang07ca at 2024/06/12 00:16
# leetgo: dev
# https://leetcode.cn/problems/account-balance-after-rounded-purchase/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/account-balance-after-rounded-purchase/solutions/2374878/yi-xing-xie-fa-by-endlesscheng-yfe2/
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10


# @lc code=end

if __name__ == "__main__":
    purchaseAmount: int = deserialize("int", read_line())
    ans = Solution().accountBalanceAfterPurchase(purchaseAmount)
    print("\noutput:", serialize(ans, "integer"))
