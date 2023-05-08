from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        result = 0

        for i in range(m):
            result += mat[i][i] + mat[i][m - 1 - i]

        if m % 2 == 1:
            result -= mat[m // 2][m // 2]

        return result
