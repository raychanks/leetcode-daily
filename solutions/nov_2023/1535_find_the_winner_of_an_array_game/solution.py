from collections import deque
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        deq = deque(arr)
        count = 0

        while count < k:
            a, b = deq.popleft(), deq.popleft()

            if a > b:
                count += 1
                deq.appendleft(a)
                deq.append(b)
            else:
                count = 1
                deq.appendleft(b)
                deq.append(a)

            if count == k:
                return deq[0]
