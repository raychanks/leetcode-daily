from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        FOUR_DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])

        groups = [[], []]
        group_idx = 0
        seen = set()
        queue = deque()

        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 0 or (r, c) in seen:
                    continue

                queue.append((r, c))

                while queue:
                    coord = queue.popleft()

                    if coord in seen:
                        continue

                    seen.add(coord)
                    is_border = False

                    for dr, dc in FOUR_DIR:
                        nr, nc = coord[0] + dr, coord[1] + dc

                        if not 0 <= nr < m or not 0 <= nc < n:
                            continue

                        if grid[nr][nc] == 0:
                            is_border = True
                            continue

                        if (nr, nc) in seen:
                            continue

                        queue.append((nr, nc))

                    if is_border:
                        groups[group_idx].append(coord)

                group_idx += 1

        min_dist = 10**9

        for coord1 in groups[0]:
            for coord2 in groups[1]:
                min_dist = min(
                    min_dist,
                    abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) - 1,
                )

        return min_dist
