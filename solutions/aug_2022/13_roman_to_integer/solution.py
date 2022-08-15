class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        denomination = 0
        result = 0

        for i in range(len(s) - 1, -1, -1):
            value = value_map[s[i]]
            denomination = max(value, denomination)
            if value < denomination:
                result -= value
            else:
                result += value

        return result
