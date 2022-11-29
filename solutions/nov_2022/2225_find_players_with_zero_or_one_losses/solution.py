from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_counter = Counter()
        seen = set()

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            lost_counter[loser] += 1

        all_win = []
        one_lost = []

        for player in seen:
            if lost_counter[player] == 0:
                all_win.append(player)
            elif lost_counter[player] == 1:
                one_lost.append(player)

        all_win.sort()
        one_lost.sort()

        return [all_win, one_lost]
