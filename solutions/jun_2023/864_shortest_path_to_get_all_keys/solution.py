from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        four_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        start = [-1, -1]
        num_keys = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    start = [r, c]
                elif cell.islower():
                    num_keys += 1

        min_steps = 10**9

        # r, c, dist, keys
        queue: deque[tuple[int, int, int, int]] = deque([(*start, 0, 0)])
        while queue:
            r, c, dist, keys = queue.popleft()

            q2 = deque([(r, c, dist, keys)])
            visited = set()

            while q2:
                r2, c2, dist2, keys2 = q2.popleft()

                if grid[r2][c2] == "#":
                    continue
                if grid[r2][c2].isupper():
                    if (1 << (ord(grid[r2][c2]) - ord("A"))) & keys2 == 0:
                        continue

                if grid[r2][c2].islower():
                    if (1 << (ord(grid[r2][c2]) - ord("a"))) & keys2 == 0:
                        n_keys2 = (1 << (ord(grid[r2][c2]) - ord("a"))) | keys2

                        if n_keys2 == (1 << num_keys) - 1:
                            min_steps = min(min_steps, dist2)
                        else:
                            queue.append((r2, c2, dist2, n_keys2))

                for dr, dc in four_dir:
                    nr, nc = r2 + dr, c2 + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    q2.append((nr, nc, dist2 + 1, keys2))

        return min_steps if min_steps != 10**9 else -1
