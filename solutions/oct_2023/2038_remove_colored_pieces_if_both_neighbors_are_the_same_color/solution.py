class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_removable, b_removable = 0, 0

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    a_removable += 1
                else:
                    b_removable += 1

        return a_removable - b_removable > 0
