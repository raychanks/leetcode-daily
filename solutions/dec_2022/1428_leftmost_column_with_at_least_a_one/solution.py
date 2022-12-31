class BinaryMatrix:
    """
    This is BinaryMatrix's API interface.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, mat) -> None:
        self.count = 0
        self.matrix = mat

    def get(self, row: int, col: int) -> int:
        self.count += 1

        if self.count > 1000:
            raise

        return self.matrix[row][col]

    def dimensions(self) -> list[int]:
        return [len(self.matrix), len(self.matrix[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        m, n = binaryMatrix.dimensions()
        appear_at_cols = [-1] * m

        for r in range(m):
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2
                val = binaryMatrix.get(r, mid)

                if val == 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    appear_at_cols[r] = mid

        min_col = n

        for col in appear_at_cols:
            if col != -1:
                min_col = min(min_col, col)

        return min_col if min_col != n else -1
