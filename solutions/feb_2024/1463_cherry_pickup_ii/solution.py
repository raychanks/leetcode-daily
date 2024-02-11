from collections import defaultdict
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        states = defaultdict(int, {(0, n - 1): grid[0][0] + grid[0][n - 1]})

        for r in range(1, m):
            next_states = defaultdict(int)

            for i, j in states.keys():
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni, nj = i + di, j + dj
                        if ni not in range(0, n) or nj not in range(0, n):
                            continue

                        num_cherry = (
                            grid[r][ni] + grid[r][nj] if ni != nj else grid[r][ni]
                        )
                        next_states[(ni, nj)] = max(
                            next_states[(ni, nj)], states[(i, j)] + num_cherry
                        )

            states = next_states

        return max(states.values())
