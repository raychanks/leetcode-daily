from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            max_len = max(max_len, i - start)

        return max_len
