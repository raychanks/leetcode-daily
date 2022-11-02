from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [-1] * n

        for c in range(n):
            x = c
            for r in range(m):
                d = grid[r][x]
                if d == 1:
                    if x == n - 1 or grid[r][x + 1] == -1:
                        break
                elif d == -1:
                    if x == 0 or grid[r][x - 1] == 1:
                        break
                x += d
            else:
                res[c] = x

        return res
