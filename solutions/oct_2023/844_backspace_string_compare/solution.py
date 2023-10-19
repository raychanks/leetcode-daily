class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptr_s, ptr_t = len(s) - 1, len(t) - 1
        remove_count_s, remove_count_t = 0, 0

        while ptr_s >= 0 or ptr_t >= 0:
            if ptr_s >= 0 and s[ptr_s] == "#":
                remove_count_s += 1
                ptr_s -= 1
                continue

            if ptr_t >= 0 and t[ptr_t] == "#":
                remove_count_t += 1
                ptr_t -= 1
                continue

            if remove_count_s > 0:
                ptr_s -= 1
                remove_count_s -= 1
                continue

            if remove_count_t > 0:
                ptr_t -= 1
                remove_count_t -= 1
                continue

            if not (ptr_s >= 0 and ptr_t >= 0) or s[ptr_s] != t[ptr_t]:
                return False

            ptr_s -= 1
            ptr_t -= 1

        return ptr_s < 0 and ptr_t < 0
