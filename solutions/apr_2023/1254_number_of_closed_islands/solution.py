from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r_idx in range(m):
            for c_idx in range(n):
                if (r_idx, c_idx) in visited:
                    continue

                if grid[r_idx][c_idx] == 1:
                    continue

                queue = deque([(r_idx, c_idx)])
                is_island = True

                while queue:
                    r, c = queue.popleft()

                    if (r, c) in visited:
                        continue

                    visited.add((r, c))

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if not (0 <= nr < m and 0 <= nc < n):
                            is_island = False
                            continue

                        if (nr, nc) in visited:
                            continue

                        if grid[nr][nc] == 0:
                            queue.append((nr, nc))

                if is_island:
                    island_count += 1

        return island_count
