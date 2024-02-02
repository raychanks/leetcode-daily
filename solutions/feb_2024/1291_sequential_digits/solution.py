from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []

        for size in range(len(str(low)), len(str(high)) + 1):
            for i in range(len(digits) - size + 1):
                num = int(digits[i : i + size])
                if low <= num <= high:
                    result.append(num)

        return result
