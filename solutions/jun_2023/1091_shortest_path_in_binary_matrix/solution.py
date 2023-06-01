from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        queue = deque([(0, 0)])
        visited = set()
        steps = 0

        while queue:
            steps += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) in visited:
                    continue

                visited.add((r, c))

                if (r, c) == (n - 1, n - 1):
                    return steps

                for dc, dr in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < n and 0 <= nc < n):
                        continue

                    if grid[nr][nc] != 0:
                        continue

                    if (nr, nc) in visited:
                        continue

                    queue.append((nr, nc))

        return -1
