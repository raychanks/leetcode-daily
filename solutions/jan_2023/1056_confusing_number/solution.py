class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        num_str = str(n)
        rotated = []

        for s in num_str[::-1]:
            if s not in mapping:
                return False

            rotated.append(mapping[s])

        return int("".join(rotated)) != n
