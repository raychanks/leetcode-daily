class TicTacToe:
    def __init__(self, n: int):
        self._dim = n
        self._row_dominance = [0] * n
        self._col_dominance = [0] * n
        self._diag_lr_dominance = 0
        self._diag_rl_dominance = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self._update_dominance(row, col, 1)
        else:
            self._update_dominance(row, col, -1)

        if (
            abs(self._row_dominance[row]) == self._dim
            or abs(self._col_dominance[col]) == self._dim
            or abs(self._diag_lr_dominance) == self._dim
            or abs(self._diag_rl_dominance) == self._dim
        ):
            return player

        return 0

    def _update_dominance(self, row, col, delta):
        self._row_dominance[row] += delta
        self._col_dominance[col] += delta

        if row == col == self._dim // 2 and self._dim % 2 == 1:
            self._diag_lr_dominance += delta
            self._diag_rl_dominance += delta
        elif row == col:
            self._diag_lr_dominance += delta
        elif row == self._dim - 1 - col:
            self._diag_rl_dominance += delta


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
