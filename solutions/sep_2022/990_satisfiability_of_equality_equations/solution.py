from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        char_sets = [DSU.make_set(chr(ord("a") + i)) for i in range(26)]

        for equation in equations:
            a, b = equation[0], equation[-1]
            is_equal = equation[1] == "="
            idx_a, idx_b = ord(a) - ord("a"), ord(b) - ord("a")

            if is_equal:
                set_a, set_b = char_sets[idx_a], char_sets[idx_b]
                DSU.union(set_a, set_b)

        for equation in equations:
            a, b = equation[0], equation[-1]
            is_equal = equation[1] == "="
            idx_a, idx_b = ord(a) - ord("a"), ord(b) - ord("a")

            if not is_equal:
                set_a, set_b = char_sets[idx_a], char_sets[idx_b]
                if DSU.find_set(set_a) is DSU.find_set(set_b):
                    return False

        return True


class DSUNode:
    def __init__(self, data) -> None:
        self.rank = 0
        self.data = data
        self.parent = self


class DSU:
    @staticmethod
    def make_set(value) -> DSUNode:
        return DSUNode(value)

    @staticmethod
    def union(node1, node2):
        parent1 = DSU.find_set(node1)
        parent2 = DSU.find_set(node2)

        if parent1 != parent2:
            representative = parent1
            to_merge = parent2
            if parent1.rank < parent2.rank:
                representative = parent2
                to_merge = parent1

            if representative.rank == to_merge.rank:
                representative.rank += 1

            to_merge.parent = representative
            to_merge.rank = 0

    @staticmethod
    def find_set(node) -> DSUNode:
        cur_node = node
        while cur_node.parent != cur_node:
            cur_node = cur_node.parent
        node.parent = cur_node
        return cur_node
