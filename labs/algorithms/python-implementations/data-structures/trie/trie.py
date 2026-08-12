"""







"""


class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.next = dict()  # str: TrieNode

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.is_leaf = True

    def insert_many(self, words):
        for word in words:
            self.insert(word)

    def find(self, word):
        cur = self
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return cur.is_leaf

    def delete(self, word):
        def _delete(cur, word, index):
            if index == len(word):
                if not cur.is_leaf:
                    return False
                cur.is_leaf = False
                return len(cur.next) == 0

            char = word[index]
            char_node = cur.next.get(char)
            if char_node is None:
                return False

            delete_cur = _delete(char_node, word, index + 1)
            if delete_cur:
                del cur.next[char]
                return len(cur.next) == 0
            return delete_cur

        _delete(self, word, 0)


def test_trie():

    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    root.insert_many(words)
    # print_words(root, "")
    assert all(root.find(word) for word in words)
    assert root.find("banana")
    assert not root.find("bandanas")
    assert not root.find("apps")
    assert root.find("apple")
    assert root.find("all")

    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")


def main():
    test_trie()


if __name__ == "__main__":
    main()
