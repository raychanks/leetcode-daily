from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        expect_increase = nums[0] < nums[-1]
        current = nums[0]

        for num in nums:
            if expect_increase and num < current:
                return False
            if not expect_increase and num > current:
                return False
            current = num

        return True
