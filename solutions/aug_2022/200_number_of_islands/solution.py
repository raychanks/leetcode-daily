from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = []
        for row in grid:
            seen.append([False] * len(row))

        directions = [
            (1, 0),  # right
            (-1, 0),  # left
            (0, 1),  # down
            (0, -1),  # up
        ]
        num_islands = 0

        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == "0" or seen[r][c]:
                    continue

                queue = [(r, c)]
                num_islands += 1

                while len(queue):
                    y, x = queue.pop()
                    seen[y][x] = True

                    for dx, dy in directions:
                        next_x = x + dx
                        next_y = y + dy

                        if next_x < 0 or next_x >= len(grid[0]):
                            continue

                        if next_y < 0 or next_y >= len(grid):
                            continue

                        if grid[next_y][next_x] == "1" and not seen[next_y][next_x]:
                            queue.append((next_y, next_x))

        return num_islands
