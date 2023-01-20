from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        seq = []

        def backtrack(idx):
            if idx == len(nums):
                if len(seq) >= 2:
                    result_set.add(tuple(seq))
                return

            num = nums[idx]

            if not seq or seq[-1] <= num:
                seq.append(num)
                backtrack(idx + 1)
                seq.pop()

            backtrack(idx + 1)

        backtrack(0)

        return list(result_set)
