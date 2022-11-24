from collections import Counter, defaultdict, deque
from itertools import chain
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def dfs(r, c, idx):
            if board[r][c] != word[idx] or (r, c) in seen:
                return False
            if idx == len(word) - 1 and board[r][c] == word[idx]:
                return True

            seen.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in seen:
                    continue

                if dfs(nr, nc, idx + 1):
                    return True

            seen.remove((r, c))

            return False

        # search from front to back is the same as back to front
        # so start with a char with smaller frequency to reduce
        # branches
        board_counter = Counter(chain(*board))
        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
