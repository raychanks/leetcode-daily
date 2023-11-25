from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        n = len(nums)
        answer = [0] * n

        for i in range(n):
            answer[i] = (
                prefix_sum[n]
                - prefix_sum[i]
                - (nums[i] * (n - i))
                + (nums[i] * i - prefix_sum[i])
            )

        return answer
