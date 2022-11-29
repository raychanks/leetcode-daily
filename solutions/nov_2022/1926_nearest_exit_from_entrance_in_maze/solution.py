from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = {tuple(entrance)}

        def is_exit(r, c):
            return (r == 0 or c == 0 or r == m - 1 or c == n - 1) and [r, c] != entrance

        queue: deque[tuple[int, int, int]] = deque([(*entrance, 0)])

        while queue:
            r, c, travelled = queue.popleft()

            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc

                if not 0 <= new_r < m or not 0 <= new_c < n:
                    continue

                if (new_r, new_c) in seen:
                    continue

                seen.add((new_r, new_c))

                if maze[new_r][new_c] == "+":
                    continue

                if is_exit(new_r, new_c):
                    return travelled + 1

                queue.append((new_r, new_c, travelled + 1))

        return -1
