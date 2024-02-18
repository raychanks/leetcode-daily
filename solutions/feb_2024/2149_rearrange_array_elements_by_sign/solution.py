from collections import deque
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = deque()
        negatives = deque()
        result = [0] * len(nums)

        for num in nums:
            if num >= 0:
                positives.append(num)
            else:
                negatives.append(num)

        for i in range(len(nums)):
            if i % 2 == 0:
                result[i] = positives.popleft()
            else:
                result[i] = negatives.popleft()

        return result
