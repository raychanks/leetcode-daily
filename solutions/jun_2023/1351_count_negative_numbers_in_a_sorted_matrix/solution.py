from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = m, 0

        while col < n:
            if row > 0 and grid[row - 1][col] < 0:
                row -= 1
            else:
                col += 1
                count += m - row

        return count
