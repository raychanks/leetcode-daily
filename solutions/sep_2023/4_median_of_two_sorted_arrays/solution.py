from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)
        is_even_len = len_sum % 2 == 0

        target_idx = len_sum // 2
        if is_even_len:
            target_idx -= 1

        idx1, idx2 = self._advance_indices(nums1, nums2, target_idx)

        return self._calculate_median(nums1, nums2, idx1, idx2)

    def _advance_indices(self, nums1, nums2, target_idx):
        idx1, idx2 = 0, 0

        while idx1 + idx2 < target_idx:
            if idx1 == len(nums1):
                idx2 += 1
            elif idx2 == len(nums2):
                idx1 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return idx1, idx2

    def _calculate_median(self, nums1, nums2, idx1, idx2):
        is_even_len = (len(nums1) + len(nums2)) % 2 == 0
        num_element_to_include = 2 if is_even_len else 1

        nums = []
        for _ in range(num_element_to_include):
            if idx1 == len(nums1):
                nums.append(nums2[idx2])
                idx2 += 1
            elif idx2 == len(nums2):
                nums.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1] < nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1
            else:
                nums.append(nums2[idx2])
                idx2 += 1

        return sum(nums) / len(nums)
