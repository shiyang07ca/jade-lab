# [1094. 拼车][link] (Medium)

[link]: https://leetcode.cn/problems/car-pooling/

车上最初有 `capacity` 个空座位。车 **只能** 向一个方向行驶（也就是说， **不允许掉头或改变方向**）

给定整数 `capacity` 和一个数组 `trips` ,  `trip[i] = [numPassengersᵢ, fromᵢ, toᵢ]` 表示第 `i` 次旅行
有 `numPassengersᵢ` 乘客，接他们和放他们的位置分别是 `fromᵢ` 和 `toᵢ` 。这些位置是从汽车的初始位置向
东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 `true`，否则请返回 `false`。

**示例 1：**

```
输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

```

**示例 2：**

```
输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true

```

**提示：**

- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengersᵢ <= 100`
- `0 <= fromᵢ < toᵢ <= 1000`
- `1 <= capacity <= 10⁵`
