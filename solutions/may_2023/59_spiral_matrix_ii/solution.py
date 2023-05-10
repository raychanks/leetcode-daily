from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        direction = "right"
        r, c = 0, 0

        for i in range(1, n**2 + 1):
            result[r][c] = i

            if direction == "right":
                if c == right:
                    direction = "down"
                    r += 1
                    top += 1
                else:
                    c += 1
            elif direction == "down":
                if r == bottom:
                    direction = "left"
                    c -= 1
                    right -= 1
                else:
                    r += 1
            elif direction == "left":
                if c == left:
                    direction = "up"
                    r -= 1
                    bottom -= 1
                else:
                    c -= 1
            elif direction == "up":
                if r == top:
                    direction = "right"
                    c += 1
                    left += 1
                else:
                    r -= 1

        return result
