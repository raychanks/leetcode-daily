from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []

        def dfs(num: int, remaining_len: int) -> List[int]:
            if remaining_len == 0:
                return [num]

            last_digit = num % 10
            result = []

            if num != 0 and last_digit + k < 10:
                result.extend(dfs(num * 10 + last_digit + k, remaining_len - 1))

            if last_digit - k >= 0:
                result.extend(dfs(num * 10 + last_digit - k, remaining_len - 1))

            return result

        for i in range(10):
            answer.extend(dfs(i, n - 1))

        answer_set = set(answer)

        if 0 in answer_set:
            answer_set.remove(0)

        return list(answer_set)
