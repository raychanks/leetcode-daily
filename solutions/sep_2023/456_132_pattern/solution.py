import math
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cur_min = math.inf
        prefix_min = []
        for num in nums:
            cur_min = min(cur_min, num)
            prefix_min.append(cur_min)

        stack = []

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            if num <= prefix_min[i]:
                continue

            if not stack or stack[-1] > num:
                stack.append(num)
                continue

            while stack and stack[-1] < num:
                if stack[-1] > prefix_min[i]:
                    return True
                stack.pop()

        return False
