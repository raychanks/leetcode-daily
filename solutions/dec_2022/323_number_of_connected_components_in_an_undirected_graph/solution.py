from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_set = set(range(n))
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = 0

        while len(node_set):
            queue = deque([node_set.pop()])
            seen = set()
            count += 1

            while queue:
                node = queue.popleft()

                if node in seen:
                    continue

                seen.add(node)
                adj_nodes = adj_list[node]

                for adj_node in adj_nodes:
                    if adj_node in node_set:
                        node_set.remove(adj_node)
                    queue.append(adj_node)

        return count
