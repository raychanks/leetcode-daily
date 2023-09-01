from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        idx = 1

        while idx <= n:
            for i in range(len(result)):
                result.append(result[i] + 1)
                idx += 1

                if idx > n:
                    break

        return result
