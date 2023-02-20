from typing import List

from templates.dsu import DSU


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        seen = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        answer = []

        for r, c in positions:
            if (r, c) in seen:
                answer.append(count)
                continue

            node = DSU.make_set((r, c))
            seen[(r, c)] = node

            parents = set()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) in seen:
                    parent = DSU.find_set(seen[(nr, nc)])
                    parents.add(parent.data)

            if not parents:
                count += 1
            else:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) in seen:
                        DSU.union(node, seen[(nr, nc)])

                merged_parents = set()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) in seen:
                        parent = DSU.find_set(seen[(nr, nc)])
                        merged_parents.add(parent.data)

                count -= len(parents) - len(merged_parents)

            answer.append(count)

        return answer
