from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        queue.append((0, 0, 0, k))  # row, col, distance, k_remaining
        k_map = [[-1] * n for _ in range(m)]

        while queue:
            r, c, d, k_remaining = queue.popleft()

            if r == m - 1 and c == n - 1:
                return d

            if grid[r][c] == 1:
                k_remaining -= 1

            for dx, dy in directions:
                nc, nr = c + dx, r + dy
                if not (0 <= nc < n and 0 <= nr < m):
                    continue

                if k_map[nr][nc] < k_remaining:
                    queue.append((nr, nc, d + 1, k_remaining))
                    k_map[nr][nc] = k_remaining

        return -1
