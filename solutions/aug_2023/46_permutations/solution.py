from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        result = []

        for i, num in enumerate(nums):
            excluded = [n for j, n in enumerate(nums) if j != i]

            for p in self.permute(excluded):
                result.append([num] + p)

        return result
