from collections import defaultdict, deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj_list = defaultdict(list)

        for src, dest in enumerate(edges):
            if dest == -1:
                continue

            adj_list[src].append(dest)

        distances1 = self.getMinDistances(n, adj_list, node1)
        distances2 = self.getMinDistances(n, adj_list, node2)

        current_min = n
        current_min_index = n

        for i, (d1, d2) in enumerate(zip(distances1, distances2)):
            if max(d1, d2) < current_min:
                current_min = max(d1, d2)
                current_min_index = i

        if current_min_index == n:
            return -1

        return current_min_index

    def getMinDistances(self, n, adj_list, node):
        distances = [n] * n
        queue = deque([node])
        distance = 0
        proximity_count = len(queue)
        seen = set()

        while queue:
            node = queue.popleft()
            proximity_count -= 1
            seen.add(node)

            distances[node] = distance

            for adj in adj_list[node]:
                if adj in seen:
                    continue

                queue.append(adj)

            if proximity_count == 0:
                distance += 1
                proximity_count = len(queue)

        return distances
