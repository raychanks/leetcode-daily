from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature, i))
                continue

            while stack:
                last_temp, last_idx = stack[-1]

                if last_temp >= temperature:
                    break

                stack.pop()
                res[last_idx] = i - last_idx

            stack.append((temperature, i))

        return res
