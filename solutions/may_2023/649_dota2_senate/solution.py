from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def solve(s):
            queue_radiant, queue_dire = deque(), deque()
            radiant_ban_count, dire_ban_count = 0, 0

            for i, party in enumerate(s):
                if party == "R":
                    if radiant_ban_count > 0:
                        radiant_ban_count -= 1
                        continue

                    dire_ban_count += 1
                    queue_radiant.append(i)
                else:
                    if dire_ban_count > 0:
                        dire_ban_count -= 1
                        continue

                    radiant_ban_count += 1
                    queue_dire.append(i)

            for _ in range(radiant_ban_count):
                if not queue_radiant:
                    return ["D"], True

                queue_radiant.popleft()

            for _ in range(dire_ban_count):
                if not queue_dire:
                    return ["R"], True

                queue_dire.popleft()

            merged = []
            is_unanimous = not len(queue_radiant) or not len(queue_dire)

            while queue_radiant or queue_dire:
                if not queue_dire:
                    merged.extend(["R"] * len(queue_radiant))
                    break
                if not queue_radiant:
                    merged.extend(["D"] * len(queue_dire))
                    break

                radiant, dire = queue_radiant[0], queue_dire[0]

                if radiant < dire:
                    queue_radiant.popleft()
                    merged.append("R")
                else:
                    queue_dire.popleft()
                    merged.append("D")

            return "".join(merged), is_unanimous

        res, is_ended = solve(senate)
        while not is_ended:
            res, is_ended = solve(res)

        return "Radiant" if res[0] == "R" else "Dire"
