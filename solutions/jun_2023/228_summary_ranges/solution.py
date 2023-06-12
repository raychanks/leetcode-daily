from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]
        prev = start

        def add_to_result():
            if prev == start:
                result.append(str(start))
            else:
                result.append(f"{start}->{prev}")

        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                add_to_result()
                start = nums[i]
                prev = start
            else:
                prev = nums[i]

        add_to_result()

        return result
