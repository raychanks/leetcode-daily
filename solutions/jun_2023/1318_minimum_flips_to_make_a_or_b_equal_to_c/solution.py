class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        digit = 1
        flip_count = 0

        while digit <= max(a, b, c):
            digit_a = a & digit
            digit_b = b & digit
            digit_c = c & digit

            if digit_a | digit_b != digit_c:
                if digit_c == 0 and digit_a == digit_b:
                    flip_count += 2
                else:
                    flip_count += 1

            digit <<= 1

        return flip_count
