#include <stdexcept>
#include <utility>
#include <vector>

class IndexedMinHeap {
public:
    int insert(int value) {
        const int insertion_id = static_cast<int>(insertion_to_heap_.size());
        values_.push_back(value);
        heap_to_insertion_.push_back(insertion_id);
        insertion_to_heap_.push_back(static_cast<int>(values_.size()) - 1);
        swim(static_cast<int>(values_.size()) - 1);
        return insertion_id;
    }

    int minimum() const {
        if (empty()) {
            throw std::out_of_range("heap is empty");
        }
        return values_[1];
    }

    bool empty() const {
        return values_.size() == 1;
    }

private:
    void swap_positions(int left, int right) {
        std::swap(insertion_to_heap_[heap_to_insertion_[left]], insertion_to_heap_[heap_to_insertion_[right]]);
        std::swap(heap_to_insertion_[left], heap_to_insertion_[right]);
        std::swap(values_[left], values_[right]);
    }

    void swim(int position) {
        while (position > 1 && values_[position] < values_[position / 2]) {
            swap_positions(position, position / 2);
            position /= 2;
        }
    }

    std::vector<int> values_{0};
    std::vector<int> heap_to_insertion_{0};
    std::vector<int> insertion_to_heap_{0};
};
