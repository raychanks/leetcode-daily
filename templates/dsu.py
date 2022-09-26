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
        compress_path_candidates = []

        while cur_node.parent != cur_node:
            compress_path_candidates.append(cur_node)
            cur_node = cur_node.parent

        for n in compress_path_candidates:
            n.parent = cur_node

        return cur_node
