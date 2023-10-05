from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        majorities = []
        candidates = {candidate1, candidate2} - {None}

        for candidate in candidates:
            if candidate is None:
                continue

            if nums.count(candidate) > len(nums) / 3:
                majorities.append(candidate)

        return majorities
