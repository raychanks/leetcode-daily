from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        left, right = 0, len(nums) // 2

        while right < len(nums):
            answer.append(nums[left])
            answer.append(nums[right])

            left += 1
            right += 1

        return answer
