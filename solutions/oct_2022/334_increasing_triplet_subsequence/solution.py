from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pair1, pair2 = [nums[0]], []

        for num in nums:
            if len(pair2):
                if num > pair2[1]:
                    return True
                if pair2[0] < num < pair2[1]:
                    pair2[1] = num

            if len(pair1) == 1:
                if num < pair1[0]:
                    pair1 = [num]
                elif num > pair1[0]:
                    pair1.append(num)
            elif len(pair1) == 2:
                if num > pair1[1]:
                    return True
                if num < pair1[0]:
                    pair2 = pair1
                    pair1 = [num]
                elif pair1[0] < num < pair1[1]:
                    pair1[1] = num

        return False
