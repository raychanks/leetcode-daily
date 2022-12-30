from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        def dfs(cur_node, path, visited):
            if cur_node == len(graph) - 1:
                result.append(path + [cur_node])
                return

            for adj in graph[cur_node]:
                if adj in visited:
                    continue

                visited.add(cur_node)
                dfs(adj, path + [cur_node], visited)
                visited.remove(cur_node)

        dfs(0, [], set())

        return result
