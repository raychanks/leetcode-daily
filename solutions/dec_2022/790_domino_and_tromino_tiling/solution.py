from functools import cache
from typing import Optional


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        @cache
        def solve(width: int, bulge_at_row: Optional[int] = None) -> int:
            if width <= 2:
                return width

            if bulge_at_row is None:
                return (
                    solve(width - 1)
                    + solve(width - 2)
                    + solve(width - 2, 0)
                    + solve(width - 2, 1)
                )

            return solve(width - 1, 1 - bulge_at_row) + solve(width - 1)

        return solve(n) % MOD
