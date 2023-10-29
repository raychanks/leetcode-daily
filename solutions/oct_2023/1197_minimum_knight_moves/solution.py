from collections import defaultdict, deque
import heapq


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [
            (-1, -2),
            (1, -2),
            (-2, -1),
            (2, -1),
            (-2, 1),
            (2, 1),
            (-1, 2),
            (1, 2),
        ]
        visited = set()
        min_heap = [(0, 0, 0)]
        step_mapping = defaultdict(lambda: 10**9)
        step_mapping[(0, 0)] = 0

        while min_heap:
            steps, x1, y1 = heapq.heappop(min_heap)

            if (x1, y1) == (x, y):
                return steps

            if (x1, y1) in visited:
                continue

            for dx, dy in moves:
                nx, ny = x1 + dx, y1 + dy

                if step_mapping[(nx, ny)] > steps + 1:
                    step_mapping[(nx, ny)] = steps + 1
                    heapq.heappush(min_heap, (steps + 1, nx, ny))

            visited.add((x1, y1))

        return -1
