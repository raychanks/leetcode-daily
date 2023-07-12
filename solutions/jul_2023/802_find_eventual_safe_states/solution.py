from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        result = {}

        def dfs(node):
            if node in visited:
                result[node] = False
                return result[node]

            if node in result:
                return result[node]

            if not graph[node]:
                result[node] = True
                return result[node]

            visited.add(node)
            is_safe = True

            for adj in graph[node]:
                if node in result and not result[node]:
                    is_safe = False
                    break

                if not dfs(adj):
                    is_safe = False
                    break

            visited.remove(node)
            result[node] = is_safe
            return result[node]

        for i in range(len(graph)):
            dfs(i)

        return sorted(k for k, v in result.items() if v)
