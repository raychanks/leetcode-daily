from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) // 4 + 1
        cur_run = 0
        cur_num = -1

        for num in arr:
            if cur_num != num:
                cur_run = 1
                cur_num = num
            else:
                cur_run += 1

            if cur_run >= target:
                return num

        return -1
