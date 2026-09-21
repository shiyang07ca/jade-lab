#include <array>
#include <stdexcept>
#include <string_view>
#include <vector>

class Trie {
public:
    Trie() : nodes_(1) {}

    void insert(std::string_view word) {
        int node = 0;
        for (char character : word) {
            int edge = to_edge(character);
            if (nodes_[node].children[edge] == -1) {
                nodes_[node].children[edge] = static_cast<int>(nodes_.size());
                nodes_.emplace_back();
            }
            node = nodes_[node].children[edge];
        }
        ++nodes_[node].terminal_count;
    }

    int count(std::string_view word) const {
        int node = 0;
        for (char character : word) {
            int edge = to_edge(character);
            node = nodes_[node].children[edge];
            if (node == -1) {
                return 0;
            }
        }
        return nodes_[node].terminal_count;
    }

private:
    struct Node {
        std::array<int, 26> children;
        int terminal_count = 0;

        Node() {
            children.fill(-1);
        }
    };

    static int to_edge(char character) {
        if (character < 'a' || character > 'z') {
            throw std::invalid_argument("trie accepts lowercase ASCII letters only");
        }
        return character - 'a';
    }

    std::vector<Node> nodes_;
};
