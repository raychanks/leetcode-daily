from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        def calculate_overlap(x_shift, y_shift, a, b):
            count1, count2 = 0, 0
            for i in range(x_shift, n):
                for j in range(y_shift, n):
                    if a[j][i] == 1 and b[j - y_shift][i - x_shift] == 1:
                        count1 += 1
                    if a[j][i - x_shift] == 1 and b[j - y_shift][i] == 1:
                        count2 += 1
            return max(count1, count2)

        for r in range(n):
            for c in range(n):
                max_overlap = max(max_overlap, calculate_overlap(c, r, img1, img2))
                max_overlap = max(max_overlap, calculate_overlap(c, r, img2, img1))

        return max_overlap
