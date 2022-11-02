from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        cur_row = matrix[0]
        for r in range(1, m):
            for c in range(1, n):
                if cur_row[c - 1] != matrix[r][c]:
                    return False
            cur_row = matrix[r]

        return True
