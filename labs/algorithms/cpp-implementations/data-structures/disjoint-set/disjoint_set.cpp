#include <numeric>
#include <stdexcept>
#include <vector>

class DisjointSet {
public:
    explicit DisjointSet(int element_count)
        : parent_(element_count), component_size_(element_count, 1) {
        if (element_count < 0) {
            throw std::invalid_argument("element_count must not be negative");
        }
        std::iota(parent_.begin(), parent_.end(), 0);
    }

    int find(int element) {
        validate(element);
        if (parent_[element] != element) {
            parent_[element] = find(parent_[element]);
        }
        return parent_[element];
    }

    bool unite(int left, int right) {
        int left_root = find(left);
        int right_root = find(right);
        if (left_root == right_root) {
            return false;
        }

        if (component_size_[left_root] < component_size_[right_root]) {
            std::swap(left_root, right_root);
        }
        parent_[right_root] = left_root;
        component_size_[left_root] += component_size_[right_root];
        return true;
    }

    bool connected(int left, int right) {
        return find(left) == find(right);
    }

    int component_size(int element) {
        return component_size_[find(element)];
    }

private:
    void validate(int element) const {
        if (element < 0 || element >= static_cast<int>(parent_.size())) {
            throw std::out_of_range("element is outside the disjoint set");
        }
    }

    std::vector<int> parent_;
    std::vector<int> component_size_;
};
