from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(target, -1, -1):
            step_size = nums[i]

            if step_size >= target - i:
                target = i

        return target == 0
