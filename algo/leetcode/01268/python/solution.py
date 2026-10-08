# Created by shiyang07ca at 2026/10/08 21:29
# leetgo: 1.4.17
# https://leetcode.cn/problems/search-suggestions-system/

from bisect import bisect_left
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def suggestedProducts(
        self,
        products: list[str],
        searchWord: str,
    ) -> list[list[str]]:
        sorted_products = sorted(products)
        answer = []
        prefix = ""

        for char in searchWord:
            prefix += char

            start = bisect_left(sorted_products, prefix)

            suggestions = []
            for product in sorted_products[start : start + 3]:
                if not product.startswith(prefix):
                    break
                suggestions.append(product)

            answer.append(suggestions)

        return answer


# @lc code=end

if __name__ == "__main__":
    products: List[str] = deserialize("List[str]", read_line())
    searchWord: str = deserialize("str", read_line())
    ans = Solution().suggestedProducts(products, searchWord)
    print("\noutput:", serialize(ans, "string[][]"))
