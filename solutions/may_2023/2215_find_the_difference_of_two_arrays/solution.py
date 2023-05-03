from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)

        list1 = list(s1 - s2)
        list2 = list(s2 - s1)

        return [list1, list2]
