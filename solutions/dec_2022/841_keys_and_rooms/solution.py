from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {0}
        queue = deque([0])

        while queue:
            room_key = queue.popleft()
            new_keys = rooms[room_key]

            for k in new_keys:
                if k not in keys:
                    keys.add(k)
                    queue.append(k)

        return len(keys) == len(rooms)
