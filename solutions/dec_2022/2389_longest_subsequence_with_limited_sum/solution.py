from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        answer = []

        for query in queries:
            current_sum = 0
            current_len = 0

            for num in nums:
                current_sum += num
                if current_sum <= query:
                    current_len += 1
                else:
                    break

            answer.append(current_len)

        return answer
