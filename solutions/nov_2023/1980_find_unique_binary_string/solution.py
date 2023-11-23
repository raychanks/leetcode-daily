from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor's Diagonal Argument
        n = len(nums)
        answer = [""] * n

        for i in range(n):
            digit = int(nums[i][i])
            answer[i] = str(digit ^ 1)

        return "".join(answer)
