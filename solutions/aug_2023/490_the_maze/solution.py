from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        direction_map = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        reachable = False

        def move(r, c, direction):
            if (r, c, direction) in visited:
                return

            dr, dc = direction_map[direction]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < m and 0 <= nc < n) or maze[nr][nc] == 1:
                if [r, c] == destination:
                    nonlocal reachable
                    reachable = True
                    return

                # stop
                for d in direction_map.keys():
                    visited.add((r, c, direction))
                    move(r, c, d)
            else:
                # continue moving
                move(nr, nc, direction)

        for d in direction_map.keys():
            move(*start, d)

        return reachable
