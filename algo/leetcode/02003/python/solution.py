from __future__ import annotations

# Created by shiyang07ca at 2023/10/31 22:37
# leetgo: dev
# https://leetcode.cn/problems/smallest-missing-genetic-value-in-each-subtree/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/smallest-missing-genetic-value-in-each-subtree/
    def smallestMissingValueSubtree(
        self, parents: list[int], nums: list[int]
    ) -> list[int]:
        n = len(parents)
        ans = [1] * n
        if 1 not in nums:  # 不存在基因值为 1 的点
            return ans

        # 建树
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)

        vis = set()

        def dfs(x: int) -> None:
            vis.add(nums[x])  # 标记基因值
            for son in g[x]:
                if nums[son] not in vis:
                    dfs(son)

        mex = 2  # 缺失的最小基因值
        node = nums.index(1)  # 出发点
        while node >= 0:
            dfs(node)
            while mex in vis:  # node 子树包含这个基因值
                mex += 1
            ans[node] = mex  # 缺失的最小基因值
            node = parents[node]  # 往上走
        return ans


# @lc code=end

if __name__ == "__main__":
    parents: list[int] = deserialize("List[int]", read_line())
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestMissingValueSubtree(parents, nums)

    print("\noutput:", serialize(ans))
