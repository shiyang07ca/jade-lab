// ref: https://www.desgard.com/algo/docs/part3/ch02/1-segment-tree-rmq/


#include <iostream>
#include <vector>
using namespace std;

const int maxn = 1e4 + 7;

vector<int> num(maxn);

int cur = 0;
int tree[maxn << 2];

void push_up(int rt) {
    tree[rt] = tree[rt << 1] + tree[rt << 1 | 1];
}

/***
 *
 * @param l 当前节点描述范围的左边界
 * @param r 当前节点描述范围的右边界
 * @param rt 代表下标，tree[rt] 代表当前节点
 */
void build(int l, int r, int rt) {
    if (l == r) {
        tree[rt] = num[cur ++];
        return ;
    }
    int m = (l + r) >> 1;
    build(l, m, rt << 1);
    build(m + 1, r, rt << 1 | 1);
    push_up(rt);
}

/***
 *
 * @param L 待查询区间左边界
 * @param R 待查询区间右边界
 * @param l 当前节点描述范围的左边界
 * @param r 当前节点描述范围的右边界
 * @param rt 代表下标，tree[rt] 代表当前节点
 */
int query(int L, int R, int l, int r, int rt) {
    if (L <= l && r <= R) {
        return tree[rt];
    }
    int m = (l + r) >> 1;
    int ret = 0;
    if (L <= m) ret += query(L, R, l, m, rt << 1);
    if (R > m)  ret += query(L, R, m + 1, r, rt << 1 | 1);
    return ret;
}

/***
    *
    * @param p 待更新的下标，指的在 num 中的下标
    * @param replace 待替换的值
    * @param l 当前节点描述范围的左边界
    * @param r 当前节点描述范围的右边界
    * @param rt 代表下标，tree[rt] 代表当前节点
    */
void update(int p, int replace, int l, int r, int rt) {
    if (l == r) {
        tree[rt] = replace;
        return ;
    }
    int m = (l + r) >> 1;
    if (p <= m) update(p, replace, l, m, rt << 1);
    else update(p, replace, m + 1, r, rt << 1 | 1);
    push_up(rt);
}

int main() {
    // [1, 8, 3, 4, 7, 1, 6, 2]
    num = vector<int>({1, 8, 3, 4, 7, 1, 6, 2});
    int n = num.size();
    build(1, n, 1);
    cout << query(1, 3, 1, n, 1) << endl; // 1 + 8 + 3 = 12
    cout << query(3, 8, 1, n, 1) << endl; // 3 + 4 + 7 + 1 + 6 + 2 = 23
    update(3, 10, 1, n, 1); // [1, 8, 10, 4, 7, 1, 6, 2]
    cout << query(1, 3, 1, n, 1) << endl; // 1 + 8 + 10 = 19
}

/*
 * 输出
 * 12
 * 23
 * 19
 *
 */
