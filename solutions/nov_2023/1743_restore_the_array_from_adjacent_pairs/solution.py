from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)
        for u, v in adjacentPairs:
            adj_list[u].add(v)
            adj_list[v].add(u)

        edge_num = 0
        for num, adj in adj_list.items():
            if len(adj) == 1:
                edge_num = num
                break

        result = []
        for _ in range(len(adj_list)):
            result.append(edge_num)

            if adj_list[edge_num]:
                next_edge = adj_list[edge_num].pop()
                adj_list[next_edge].remove(edge_num)
                edge_num = next_edge

        return result
