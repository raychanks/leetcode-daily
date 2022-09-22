from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer: List[int] = []

        for val, idx in queries:
            original_val = nums[idx]
            new_val = nums[idx] + val

            if original_val % 2 == 0:
                even_sum -= original_val
            if new_val % 2 == 0:
                even_sum += new_val

            nums[idx] = new_val
            answer.append(even_sum)

        return answer
