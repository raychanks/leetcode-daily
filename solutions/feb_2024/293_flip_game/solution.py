from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []

        valid_next_state = []

        for i in range(0, len(currentState) - 1):
            if currentState[i] != "+" or currentState[i] != currentState[i + 1]:
                continue

            valid_next_state.append(currentState[:i] + "-" * 2 + currentState[i + 2 :])

        return valid_next_state
