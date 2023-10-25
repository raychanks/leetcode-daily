from collections import deque
import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        positions = deque()

        cur_k = k
        for _ in range(n, 0, -1):
            positions.appendleft(cur_k)
            cur_k = math.ceil(cur_k / 2)

        answer = 0
        for position in positions:
            if position % 2 == 0:
                answer ^= 1

        return answer
