class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]

        ROWS, COLS = 4, 3
        dp = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0],
        ]

        for _ in range(n - 1):
            next_dp = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]

            for r in range(len(next_dp)):
                for c in range(len(next_dp[0])):
                    if r == ROWS - 1 and c in {0, COLS - 1}:
                        continue

                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc

                        if nr not in range(ROWS) or nc not in range(COLS):
                            continue

                        next_dp[r][c] += dp[nr][nc] % MOD

            dp = next_dp

        return sum(sum(row) for row in dp) % MOD
