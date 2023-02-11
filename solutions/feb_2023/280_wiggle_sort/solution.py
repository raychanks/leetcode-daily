from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ####################
        # Time: O(n log n)
        # Space: O(n)
        ####################
        # nums_sorted = sorted(nums)
        # left, right = 0, len(nums) - 1
        # idx = 0

        # while left <= right:
        #     nums[idx] = nums_sorted[left]

        #     if idx + 1 < len(nums):
        #         nums[idx + 1] = nums_sorted[right]

        #     idx += 2
        #     left += 1
        #     right -= 1

        ####################
        # Time: O(n)
        # Space: O(1)
        ####################
        def compare(idx1, idx2):
            if idx1 % 2 == 0:
                return nums[idx1] <= nums[idx2]
            return nums[idx1] >= nums[idx2]

        for i in range(len(nums) - 1):
            if compare(i, i + 1):
                i += 1
                continue

            nums[i], nums[i + 1] = nums[i + 1], nums[i]
