from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        num_set = set()
        min_num, max_num = arr[0], arr[0]

        for num in arr:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
            num_set.add(num)

        difference, mod = divmod(max_num - min_num, len(arr) - 1)

        if mod != 0:
            return False

        cur = min_num

        for _ in range(len(arr) - 1):
            cur += difference
            if cur not in num_set:
                return False

        return True
