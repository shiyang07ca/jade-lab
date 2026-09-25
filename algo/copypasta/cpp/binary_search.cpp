#include <functional>

// 在半开区间 [left, right) 中寻找第一个使 predicate 为真的整数。
// predicate 必须单调地由 false 变为 true；若区间内都为 false，则返回 right。
int first_true(int left, int right, const std::function<bool(int)>& predicate) {
    while (left < right) {
        int middle = left + (right - left) / 2;
        if (predicate(middle)) {
            right = middle;
        } else {
            left = middle + 1;
        }
    }
    return left;
}

// 在闭区间 [left, right] 中寻找最后一个使 predicate 为真的整数。
// predicate 必须单调地由 true 变为 false，且调用前须保证 predicate(left) 为 true。
int last_true(int left, int right, const std::function<bool(int)>& predicate) {
    while (left < right) {
        int middle = left + (right - left + 1) / 2;
        if (predicate(middle)) {
            left = middle;
        } else {
            right = middle - 1;
        }
    }
    return left;
}
