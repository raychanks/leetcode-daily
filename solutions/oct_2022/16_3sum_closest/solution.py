from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])

        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum == target:
                    return target

                if abs(target - three_sum) < abs(target - closest):
                    closest = three_sum

                if three_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
