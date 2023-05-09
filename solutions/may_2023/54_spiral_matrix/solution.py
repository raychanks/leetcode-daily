from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        ri = 0
        result = [0] * (m * n)

        direction = "right"
        t, b, l, r = 0, m - 1, 0, n - 1

        while ri < m * n:
            result[ri] = matrix[i][j]

            if direction == "right":
                if j == r:
                    direction = "down"
                    t += 1
                    i += 1
                else:
                    j += 1
            elif direction == "down":
                if i == b:
                    direction = "left"
                    r -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == "left":
                if j == l:
                    direction = "up"
                    b -= 1
                    i -= 1
                else:
                    j -= 1
            elif direction == "up":
                if i == t:
                    direction = "right"
                    l += 1
                    j += 1
                else:
                    i -= 1

            ri += 1

        return result
