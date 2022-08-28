import copy
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        result = copy.deepcopy(mat)

        for row_idx in range(len(mat)):
            diag = []
            diff = 0
            next_row_idx = row_idx + diff

            while next_row_idx < len(mat) and diff < len(mat[0]):
                diag.append(mat[next_row_idx][diff])
                diff += 1
                next_row_idx = row_idx + diff

            sorted_diag = sorted(diag)
            for idx, num in enumerate(sorted_diag):
                result[row_idx + idx][idx] = num

        for col_idx in range(len(mat[0])):
            diag = []
            diff = 0
            next_col_idx = col_idx + diff

            while next_col_idx < len(mat[0]) and diff < len(mat):
                diag.append(mat[diff][next_col_idx])
                diff += 1
                next_col_idx = col_idx + diff

            sorted_diag = sorted(diag)
            for idx, num in enumerate(sorted_diag):
                result[idx][col_idx + idx] = num

        return result
