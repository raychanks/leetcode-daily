from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distances = [[10**9] * n for _ in range(m)]
        ones: list[tuple[int, int]] = []
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ones.append((r, c))
                    distances[r][c] = 0

        if not ones or len(ones) == m * n:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue: deque[tuple[int, int, int]] = deque([(r, c, 0) for r, c in ones])

        while queue:
            r, c, d = queue.popleft()

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if (nr, nc) in visited:
                    continue

                if grid[nr][nc] == 1:
                    continue

                if distances[nr][nc] < d + 1:
                    continue

                distances[nr][nc] = d + 1
                queue.append((nr, nc, d + 1))

        return max(max(row) for row in distances)
