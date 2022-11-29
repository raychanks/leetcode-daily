from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        DIM = 9

        blocks = [set() for _ in range(DIM)]
        rows = [set() for _ in range(DIM)]
        cols = [set() for _ in range(DIM)]

        for r in range(DIM):
            for c in range(DIM):
                val = board[r][c]
                if val == ".":
                    continue

                block_idx = c // 3 + 3 * (r // 3)

                if val in rows[r] or val in cols[c] or val in blocks[block_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                blocks[block_idx].add(val)

        return True
