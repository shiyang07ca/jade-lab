from __future__ import annotations

# Created by shiyang07ca at 2024/04/21 12:23
# leetgo: dev
# https://leetcode.cn/problems/combination-sum-iii/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    def combinationSum31(self, k: int, n: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i, left):
            if left == 0 and len(path) == k:
                ans.append(path[:])
                return

            if i == 10 or left < i:
                return

            path.append(i)
            dfs(i + 1, left - i)
            path.pop()

            dfs(i + 1, left)

        dfs(1, n)
        return ans

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # 从 1～9 中选出恰好 k 个不同的数，使它们的和等于 n。
        # 只按严格递增的顺序选数，既避免重复使用数字，也避免重复组合。
        # 例如 k=3、n=9，答案为 [1,2,6]、[1,3,5]、[2,3,4]。
        ans: list[list[int]] = []
        path: list[int] = []

        def dfs(start: int, remain: int) -> None:
            # path：当前已选的数；start：下一个数的下界；remain：还差的和。
            # 选满 k 个数就必须结束，只有剩余和为 0 时才记录答案。
            if len(path) == k:
                if remain == 0:
                    # 后续还会修改 path，因此保存此刻的副本。
                    ans.append(path.copy())
                return

            for x in range(start, 10):
                # 所有候选数都是正数。x 已超出剩余和，后面更大的数也不行。
                if x > remain:
                    break

                path.append(x)          # 选择 x。
                dfs(x + 1, remain - x)   # 下一层只选比 x 大的数。
                path.pop()              # 当前分支结束，撤销 x，再尝试下一个数。

        # 例如 path=[1,2] 时调用 dfs(3,6)，尝试完后恢复到 [1,2]；
        # 返回上一层再 pop 掉 2，恢复到 [1]，才能继续尝试 [1,3]。
        # 候选数字只有 9 个，共 2^9 个子集；递归深度最多 k。
        # 不计返回答案，额外空间为 O(k)。
        dfs(1, n)
        return ans


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().combinationSum3(k, n)
    print("\noutput:", serialize(ans, "integer[][]"))
