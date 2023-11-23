from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        l, r = 0, 0
        max_freq = 1

        for r in range(len(nums)):
            width = r - l + 1
            changes = width * nums[r] - prefix_sum[r + 1] + prefix_sum[l]

            while changes > k:
                l += 1
                width = r - l + 1
                changes = width * nums[r] - prefix_sum[r + 1] + prefix_sum[l]

            max_freq = max(max_freq, width)

        return max_freq
