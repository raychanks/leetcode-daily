from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)
        cur_sum = 0
        num_elements = 2 * k + 1

        if len(nums) < num_elements:
            return result

        for i in range(num_elements):
            cur_sum += nums[i]

        result[k] = cur_sum // num_elements

        for i in range(num_elements, len(nums)):
            incoming = nums[i]
            outgoing = nums[i - num_elements]
            cur_sum += incoming - outgoing
            result[i - k] = cur_sum // num_elements

        return result
