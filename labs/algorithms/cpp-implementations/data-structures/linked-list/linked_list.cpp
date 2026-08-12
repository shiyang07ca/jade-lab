#include <optional>
#include <vector>

class ArrayLinkedList {
public:
    void insert_front(int value) {
        values_.push_back(value);
        next_.push_back(head_);
        head_ = static_cast<int>(values_.size()) - 1;
    }

    std::optional<int> remove_front() {
        if (head_ == -1) {
            return std::nullopt;
        }
        int value = values_[head_];
        head_ = next_[head_];
        return value;
    }

    std::vector<int> values() const {
        std::vector<int> result;
        for (int node = head_; node != -1; node = next_[node]) {
            result.push_back(values_[node]);
        }
        return result;
    }

private:
    int head_ = -1;
    std::vector<int> values_;
    std::vector<int> next_;
};
