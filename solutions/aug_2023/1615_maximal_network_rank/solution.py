from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_set = {}
        for i in range(n):
            adj_set[i] = set()
        for a, b in roads:
            adj_set[a].add(b)
            adj_set[b].add(a)

        city_connections = [(len(adj), city) for city, adj in adj_set.items()]
        city_connections.sort(reverse=True)

        max_rank = 0

        for i, connection_1 in enumerate(city_connections):
            for j in range(i + 1, len(city_connections)):
                connection_2 = city_connections[j]
                rank = connection_1[0] + connection_2[0]
                if connection_1[1] in adj_set[connection_2[1]]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank
