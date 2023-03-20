from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        prev = 0
        count = 0

        for i in range(1, len(flowerbed) - 1):
            cur_val, next_val = flowerbed[i], flowerbed[i + 1]

            if cur_val == 1 or next_val == 1:
                prev = cur_val
                continue

            if prev == 0 and cur_val == 0 and next_val == 0:
                count += 1
                prev = 1
            else:
                prev = cur_val

        return count >= n
