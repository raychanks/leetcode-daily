from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        ptr = n - 2
        taken = 0

        for _ in range(n // 3):
            taken += piles[ptr]
            ptr -= 2

        return taken
