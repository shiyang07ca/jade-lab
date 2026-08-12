#include <stdexcept>
#include <vector>

class ForwardStarGraph {
public:
    explicit ForwardStarGraph(int vertex_count) : heads_(vertex_count, -1) {
        if (vertex_count < 0) {
            throw std::invalid_argument("vertex_count must not be negative");
        }
    }

    void add_edge(int from, int to) {
        validate_vertex(from);
        validate_vertex(to);
        edges_.push_back(to);
        next_.push_back(heads_[from]);
        heads_[from] = static_cast<int>(edges_.size()) - 1;
    }

    std::vector<int> adjacent_vertices(int vertex) const {
        validate_vertex(vertex);
        std::vector<int> result;
        for (int edge = heads_[vertex]; edge != -1; edge = next_[edge]) {
            result.push_back(edges_[edge]);
        }
        return result;
    }

private:
    void validate_vertex(int vertex) const {
        if (vertex < 0 || vertex >= static_cast<int>(heads_.size())) {
            throw std::out_of_range("vertex is outside the graph");
        }
    }

    std::vector<int> heads_;
    std::vector<int> edges_;
    std::vector<int> next_;
};
