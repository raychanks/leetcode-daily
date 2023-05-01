from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        low, high = salary[0], salary[0]
        total = 0

        for num in salary:
            low = min(low, num)
            high = max(high, num)
            total += num

        return (total - low - high) / (len(salary) - 2)
