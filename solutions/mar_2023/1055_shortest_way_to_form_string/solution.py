class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        target_idx = 0
        count = 0

        while target_idx < len(target):
            has_match = False

            for source_idx in range(len(source)):
                if target_idx == len(target):
                    break

                char = target[target_idx]
                src_char = source[source_idx]

                if src_char == char:
                    target_idx += 1
                    has_match = True

            if not has_match:
                return -1

            count += 1

        return count
