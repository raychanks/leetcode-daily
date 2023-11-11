import heapq
import math
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = {i: [] for i in range(n)}
        for edge in edges:
            self.addEdge(edge)

        self.cache = {}

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adj_list[u].append((v, w))
        self.cache = {}

    def shortestPath(self, node1: int, node2: int) -> int:
        if (node1, node2) not in self.cache:
            distance = self._dijkstra(node1, node2)
            if distance == math.inf:
                distance = -1
            self.cache[(node1, node2)] = distance

        return self.cache[(node1, node2)]

    def _dijkstra(self, node1: int, node2: int):
        n = len(self.adj_list)
        distances = {i: math.inf for i in range(n)}
        min_heap = [(0, node1)]
        visited = set()

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            if distance >= distances[node]:
                continue

            distances[node] = distance

            if node == node2:
                break

            for adj, cost in self.adj_list[node]:
                heapq.heappush(min_heap, (distance + cost, adj))

            visited.add(node)

        return distances[node2]
