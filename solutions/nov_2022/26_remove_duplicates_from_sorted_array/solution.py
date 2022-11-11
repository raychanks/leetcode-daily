from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0

        for num in nums:
            if nums[ptr] != num:
                ptr += 1
                nums[ptr] = num

        return ptr + 1
