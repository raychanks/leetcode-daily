from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        PUSH, POP = "Push", "Pop"
        i = 0
        ops = []

        for num in range(1, n + 1):
            if i == len(target):
                break

            if num < target[i]:
                ops.extend([PUSH, POP])
            elif num == target[i]:
                ops.append(PUSH)
                i += 1

        return ops
