from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        idx = 0
        next_num = 1

        while count < k and idx < len(arr):
            if arr[idx] != next_num:
                count += 1
            else:
                idx += 1

            if count != k:
                next_num += 1

        if count < k:
            next_num += k - count - 1

        return next_num
