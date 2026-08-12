#include <functional>

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
