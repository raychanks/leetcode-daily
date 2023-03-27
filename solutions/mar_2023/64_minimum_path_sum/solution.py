from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev_row = [10**9] * n
        prev_row[0] = 0

        for i in range(m):
            cur_row = [0] * n

            for j in range(n):
                val = grid[i][j]

                if j > 0:
                    cur_row[j] = min(prev_row[j], cur_row[j - 1]) + val
                else:
                    cur_row[j] = prev_row[j] + val

            prev_row = cur_row

        return prev_row[-1]
