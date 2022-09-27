class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        cur_dir = "L"
        prev_idx = 0
        result = list(dominoes)

        for i, d in enumerate(dominoes):
            if d == ".":
                continue

            if cur_dir == "L":
                if d == "L":
                    for j in range(prev_idx, i):
                        result[j] = "L"
                elif d == "R":
                    cur_dir = "R"
            elif cur_dir == "R":
                if d == "L":
                    cur_dir = "L"
                    for j in range((i - prev_idx) // 2):
                        result[prev_idx + j] = "R"
                        result[i - j - 1] = "L"
                elif d == "R":
                    for j in range(prev_idx, i):
                        result[j] = "R"

            prev_idx = i + 1

        if cur_dir == "R":
            for j in range(prev_idx, len(dominoes)):
                result[j] = "R"

        return "".join(result)
