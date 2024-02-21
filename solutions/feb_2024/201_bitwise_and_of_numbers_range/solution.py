class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifted = 0

        while left != right:
            left >>= 1
            right >>= 1
            shifted += 1

        return left << shifted
