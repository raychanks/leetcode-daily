from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(current, picked_nums):
            if len(picked_nums) == k:
                result.append(picked_nums[:])
                return

            if current > n:
                return

            backtrack(current + 1, picked_nums)

            picked_nums.append(current)
            backtrack(current + 1, picked_nums)
            picked_nums.pop()

        backtrack(1, [])

        return result
