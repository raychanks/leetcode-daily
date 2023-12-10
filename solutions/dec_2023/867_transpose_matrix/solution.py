from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                transposed[c][r] = matrix[r][c]

        return transposed
