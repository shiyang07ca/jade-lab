"""
"""

################ 背包问题 ################

"""

0-1 背包 (n 个物品，背包容量为 c)
状态：从前 i 个物品中选择若干个，当容量限制为 j 时能获得的最大价值和  i∈[0,n-1], j∈[0, c]
初始值：f(0,j)=0  j∈[0, c]
除开初始状态，每个状态有两个来源，决策为 max：
   - 不选第 i 个物品：f(i-1,j) -> f(i,j)
   - 选第 i 个物品：f(i-1,j-wi)+vi -> f(i,j)   j≥wi
最优解为 f(n-1, c)

dfs(i, c) = dfs(i-1, c), dfs(i-1, c-w[i])

f[i][c] = f[i-1][c] + f[i-1][c-w[i]]
f[i+1][c] = f[i][c] + f[i][c-w[i]]

常见变形：至多装 c，求方案数/最大价值和
          恰好装 c，求方案数/最大/最小价值和
          至少装 c，求方案数/最小价值和

https://oi-wiki.org/dp/knapsack/
模板题 https://www.luogu.com.cn/problem/P1048
       https://atcoder.jp/contests/dp/tasks/dp_d
转换 LC494 https://leetcode.cn/problems/target-sum/
	   https://atcoder.jp/contests/abc274/tasks/abc274_d
"""


def zero_one_knapsack(c: int, w: List[int], v: List[int]) -> int:
    n = len(w)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i - 1, c)
        return max(dfs(i - 1, c), dfs(i - 1, c - w[i]) + v[i])

    return dfs(n - 1, c)


"""
完全背包
https://www.luogu.com.cn/problem/P1616
至少 https://www.luogu.com.cn/problem/P2918
恰好装满 LC322 https://leetcode-cn.com/problems/coin-change/
EXTRA: 恰好装满+打印方案 LC1449 https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
"""
