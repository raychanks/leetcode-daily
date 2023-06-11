class SnapshotArray:
    def __init__(self, length: int):
        self.data: list[list[tuple[int, int]]] = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        _, version = self.data[index][-1]

        if version == self.snap_id:
            self.data[index][-1] = (val, self.snap_id)
        else:
            self.data[index].append((val, self.snap_id))

    def snap(self) -> int:
        sid = self.snap_id
        self.snap_id += 1
        return sid

    def get(self, index: int, snap_id: int) -> int:
        versions = self.data[index]
        left, right = 0, len(versions) - 1

        while left <= right:
            if left == len(versions) - 1:
                return versions[left][0]

            mid = (left + right) // 2
            _, version = versions[mid]
            _, next_version = versions[mid + 1]

            if version <= snap_id < next_version:
                return versions[mid][0]

            if version <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return versions[left][0]
