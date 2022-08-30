from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        size = len(matrix)

        for r in range(size):
            for c in range(r, size):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def reflect(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        mid = size // 2

        for r in range(size):
            for c in range(mid):
                matrix[r][c], matrix[r][size - c - 1] = (
                    matrix[r][size - c - 1],
                    matrix[r][c],
                )
