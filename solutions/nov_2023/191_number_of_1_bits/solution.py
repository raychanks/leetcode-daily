class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = 1

        for _ in range(32):
            if n & num != 0:
                count += 1
            num <<= 1

        return count
