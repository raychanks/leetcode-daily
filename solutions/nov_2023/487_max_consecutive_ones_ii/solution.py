from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros = []
        one_idx = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)

                if len(zeros) == 2:
                    max_len = max(max_len, i - one_idx)
                    idx = zeros.pop(0)
                    one_idx = idx + 1

        max_len = max(max_len, len(nums) - one_idx)

        return max_len
