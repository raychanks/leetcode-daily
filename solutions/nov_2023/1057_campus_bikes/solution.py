from typing import List


class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        def calc_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        pairs = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                pairs.append((calc_distance(worker, bike), i, j))

        pairs.sort()

        used_bike = set()
        answer = [-1] * len(workers)

        for _, worker_idx, bike_idx in pairs:
            if bike_idx in used_bike or answer[worker_idx] != -1:
                continue

            answer[worker_idx] = bike_idx
            used_bike.add(bike_idx)

        return answer
