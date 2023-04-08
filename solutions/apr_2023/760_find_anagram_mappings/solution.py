from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {num: i for i, num in enumerate(nums2)}

        return [indices[num] for num in nums1]
