from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            count = 0
            cur = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] <= cur:
                    continue

                count += dfs(dr, dc)

            return count

        for r in range(m):
            for c in range(n):
                count += dfs(r, c)

        return count % mod
