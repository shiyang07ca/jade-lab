"""Prefix trie for strings."""


class Trie:
    _END = object()

    def __init__(self) -> None:
        self._root: dict[str | object, dict] = {}

    def insert(self, word: str) -> None:
        node = self._root
        for character in word:
            node = node.setdefault(character, {})
        node[self._END] = {}

    def contains(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and self._END in node

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, text: str) -> dict | None:
        node = self._root
        for character in text:
            child = node.get(character)
            if child is None:
                return None
            node = child
        return node

    def remove(self, word: str) -> bool:
        """Remove a stored word and return whether it existed."""

        def remove_from(node: dict, index: int) -> tuple[bool, bool]:
            if index == len(word):
                if self._END not in node:
                    return False, False
                del node[self._END]
                return True, not node
            character = word[index]
            child = node.get(character)
            if child is None:
                return False, False
            removed, delete_child = remove_from(child, index + 1)
            if delete_child:
                del node[character]
            return removed, not node

        removed, _ = remove_from(self._root, 0)
        return removed
