class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t != 1

        diag = min(abs(sx - fx), abs(sy - fy))
        horizontal = abs(sx - fx) - diag
        vertical = abs(sy - fy) - diag

        return t >= horizontal + vertical + diag
