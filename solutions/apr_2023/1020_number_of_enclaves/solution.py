from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        visited = set()
        total_count = 0

        for r_idx in range(m):
            for c_idx in range(n):
                if (r_idx, c_idx) in visited or grid[r_idx][c_idx] == 0:
                    continue

                is_closed = True
                queue = deque([(r_idx, c_idx)])
                count = 0

                while queue:
                    r, c = queue.popleft()

                    if (r, c) in visited:
                        continue

                    visited.add((r, c))

                    if grid[r][c] == 0:
                        continue

                    count += 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (nr, nc) in visited:
                            continue

                        if not (0 <= nr < m and 0 <= nc < n):
                            is_closed = False
                            continue

                        queue.append((nr, nc))

                if is_closed:
                    total_count += count

        return total_count
