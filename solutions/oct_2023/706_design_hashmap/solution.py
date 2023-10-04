class MyHashMap:
    num_buckets = 1009

    def __init__(self):
        self.buckets = [[] for _ in range(self.num_buckets)]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for i, (original_key, _) in enumerate(bucket):
            if original_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        for original_key, value in self._get_bucket(key):
            if original_key == key:
                return value

        return -1

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        idx_to_remove = -1

        for i, (original_key, _) in enumerate(bucket):
            if original_key == key:
                idx_to_remove = i
                break

        if idx_to_remove != -1:
            bucket.pop(idx_to_remove)

    def _get_bucket(self, key: int):
        return self.buckets[key % self.num_buckets]
