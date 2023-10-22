from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_min = nums[k]
        max_score = nums[k]
        left, right = k, k

        while left > 0 or right < n - 1:
            left_val = nums[left - 1] if left > 0 else 0
            right_val = nums[right + 1] if right < n - 1 else 0

            if left_val > right_val:
                left -= 1
                cur_min = min(cur_min, nums[left])
            else:
                right += 1
                cur_min = min(cur_min, nums[right])

            max_score = max(max_score, cur_min * (right - left + 1))

        return max_score
