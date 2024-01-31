from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((temp, i))

        return result
