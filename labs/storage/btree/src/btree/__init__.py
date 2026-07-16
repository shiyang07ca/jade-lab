"""
# Ref: https://gist.github.com/eatonphil/51b91bb30bc7dbebd9bfb3c33248e563


Resources that helped out:
https://webdocs.cs.ualberta.ca/~holte/T26/ins-b-tree.html
https://www.cs.usfca.edu/~galles/visualization/BTree.html
https://sites.radford.edu/~nokie/classes/360/trees.b.tree.html
http://carlosproal.com/ir/papers/p121-comer.pdf
https://w6113.github.io/files/papers/btreesurvey-graefe.pdf


TODO:
B Tree

B树的以下特性:
- 所有叶子节点都在同一层
- 节点中的键是有序的
- 每个节点的子节点数量不超过阶数
- 非根节点至少半满
- 所有的数据都存储在叶子节点中


假设B树的阶数（order）为 M

1. 节点的最大元素数是 M-1
2. 节点的最大子节点数是 M
3. 非根节点的最小元素数是 ⌈M/2⌉-1
4. 当节点中的元素数达到 M 时，需要进行分裂操作

例如：如果阶数为3，则非根节点至少要有1个键，最多有2个键
"""

import math
import uuid


class BTreeNode:
    def __init__(self, order=3):
        self.id = str(uuid.uuid4())[:8]
        self.order = order
        if self.order < 3:
            raise Exception("BTree must have at least 2 children.")
        self.elements = [None for _ in range(order - 1)]
        self.children = [None for _ in range(order)]

    def walk(self, fn, level=0, parent_id=None):
        assert len(self.children) == self.order
        assert len(self.elements) == self.order - 1
        assert self.order >= 3

        for i, child in enumerate(self.children):
            if child is not None:
                child.walk(fn, level + 1, self.id)

            if i < len(self.elements):
                el = self.elements[i]
                if el is None:
                    continue

                fn(el, level, self.id, parent_id)

    def contains(self, key):
        for i, child in enumerate(self.children):
            if i < len(self.elements):
                ele = self.elements[i]
                if ele is not None:
                    if key == ele["key"]:
                        return True
                    elif key < ele["key"] and child is not None:
                        return child.contains(key)
                elif child is not None:
                    return child.contains(key)
            elif child is not None:
                return child.contains(key)

        return False

    def list(self):
        lst = []

        def _tolist(node, *args):
            lst.append(node)

        self.walk(_tolist)

        return lst

    def split(self, copy, children_copy):
        left_elements = copy[: self.order // 2]
        right_elements = copy[self.order // 2 + 1 :]

        left = BTreeNode(self.order)

        left.elements[: self.order // 2] = left_elements
        left_children = children_copy[: self.order // 2 + 1]
        left.children[: len(left_children)] = left_children
        assert len(left.elements) == self.order - 1
        assert len(left.children) == self.order

        middle = copy[self.order // 2]

        right = BTreeNode(self.order)
        right.elements[: len(right_elements)] = right_elements
        right_children = children_copy[self.order // 2 + 1 :]
        right.children[: len(right_children)] = right_children
        assert len(right.elements) == self.order - 1
        assert len(right.children) == self.order
        return None, middle, left, right

    def insert_leaf(self, toinsert):
        copy = self.elements.copy()
        location_to_insert = 0
        for e in copy:
            if e is None or toinsert["key"] < e["key"]:
                break
            location_to_insert += 1

        copy.insert(location_to_insert, toinsert)

        children_copy = self.children.copy()
        children_copy.insert(location_to_insert, None)

        has_space = self.elements.count(None) > 0
        if has_space:
            new_self = BTreeNode(self.order)
            assert copy[-1] is None
            copy.pop()
            new_self.elements = copy
            assert len(new_self.elements) == new_self.order - 1

            assert children_copy[-1] is None
            children_copy.pop()
            new_self.children = children_copy
            assert len(new_self.children) == new_self.order

            return new_self, None, None, None

        # Otherwise, no space, let's split.
        return self.split(copy, children_copy)

    def insert_child(self, toinsert, i, child):
        new_self = BTreeNode(self.order)
        new_self.elements = self.elements.copy()
        new_self.children = self.children.copy()

        ret, middle, left, right = child.insert(toinsert)
        if middle is None:  # 子节点没有分裂
            new_self.children[i] = ret
            return new_self, None, None, None

        # No space, we must split.
        location_to_insert = 0
        for e in new_self.elements:
            if e is None or toinsert["key"] < e["key"]:
                break
            location_to_insert += 1

        new_self.elements.insert(location_to_insert, middle)
        new_self.children.insert(location_to_insert, None)
        assert sorted(
            [x["key"] if x is not None else math.inf for x in new_self.elements]
        ) == [x["key"] if x is not None else math.inf for x in new_self.elements]

        new_self.children[location_to_insert] = left
        new_self.children[location_to_insert + 1] = right

        has_space = self.elements.count(None) > 0
        if has_space:
            assert new_self.elements[-1] is None
            new_self.elements.pop()
            assert len(new_self.elements) == new_self.order - 1

            assert new_self.children[-1] is None
            new_self.children.pop()
            assert len(new_self.children) == new_self.order

            return new_self, None, None, None

        # No space, let's split.
        return self.split(new_self.elements, new_self.children)

    def insert(self, toinsert):
        is_leaf = self.children.count(None) == len(self.children)
        if is_leaf:
            return self.insert_leaf(toinsert)

        for i, child in enumerate(self.children):
            # 如果当前位置的元素为空, 或新键小于当前元素
            if i < len(self.elements):
                if (
                    self.elements[i] is None
                    or toinsert["key"] < self.elements[i]["key"]
                ):
                    return self.insert_child(toinsert, i, child)
            # 处理最后一个子节点
            elif child is not None:
                return self.insert_child(toinsert, i, child)

        raise AssertionError()


class BTree:
    def __init__(self, order=3):
        self.root = BTreeNode(order)

    def insert(self, toinsert):
        all_elements = self.list()

        new_self = BTree(self.root.order)
        new_node, middle, left, right = self.root.insert(toinsert)
        if middle is None:
            assert new_node is not None
            new_self.root = new_node
        else:
            # Otherwise, split at root.
            new_self.root.elements[0] = middle
            new_self.root.children[0] = left
            new_self.root.children[1] = right

        all_elements.append(toinsert)
        for el in all_elements:
            assert new_self.contains(
                el["key"]
            ), f"Expected {el} in {new_self.list()}\n{new_self.print()}"

        return new_self

    def contains(self, key):
        return self.root.contains(key)

    def list(self):
        return self.root.list()

    def print(self):
        def _print(node, level, self_id, parent_id):
            print([self_id, parent_id], " " * (level + 1) + str(node))

        print("[")
        self.root.walk(_print)
        print("]")
