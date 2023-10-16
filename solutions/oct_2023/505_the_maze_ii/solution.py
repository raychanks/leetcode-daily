from collections import deque
from typing import List


class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        m, n = len(maze), len(maze[0])
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        queue = deque([(*start, 0)])
        visited = {}
        min_distance = 10**9

        while queue:
            r, c, distance = queue.popleft()

            if visited.get((r, c), 10**9) <= distance:
                continue

            if [r, c] == destination:
                min_distance = min(min_distance, distance)
                continue

            visited[(r, c)] = distance

            for direction in directions:
                nr, nc = r, c
                dr, dc = directions[direction]
                dist = 0

                while (
                    (nr + dr) in range(m)
                    and (nc + dc) in range(n)
                    and maze[nr + dr][nc + dc] == 0
                ):
                    nr += dr
                    nc += dc
                    dist += 1

                if dist:
                    queue.append((nr, nc, distance + dist))

        return min_distance if min_distance != 10**9 else -1
