from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        amount = 0
        max_from_right = [0] * len(height)
        cur_max_right = 0

        for i in range(len(height) - 1, 0, -1):
            cur_max_right = max(cur_max_right, height[i])
            max_from_right[i - 1] = cur_max_right

        max_left = 0

        for i, num in enumerate(height):
            max_right = max_from_right[i]
            min_left_right = min(max_left, max_right)

            if min_left_right > num:
                amount += min_left_right - num

            max_left = max(max_left, num)

        return amount
