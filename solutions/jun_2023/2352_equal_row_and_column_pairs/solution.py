from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = defaultdict(int)
        size = len(grid)
        count = 0

        for col_idx in range(size):
            col = []

            for row_idx in range(size):
                col.append(str(grid[row_idx][col_idx]))

            col_str = ",".join(col)
            cols[col_str] += 1

        for row_idx in range(size):
            row = []

            for col_idx in range(size):
                row.append(str(grid[row_idx][col_idx]))

            row_str = ",".join(row)

            if row_str in cols:
                count += cols[row_str]

        return count
