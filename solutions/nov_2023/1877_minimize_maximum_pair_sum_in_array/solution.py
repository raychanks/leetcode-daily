from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = nums[0] + nums[-1]

        for i in range(n // 2):
            answer = max(answer, nums[i] + nums[n - 1 - i])

        return answer
