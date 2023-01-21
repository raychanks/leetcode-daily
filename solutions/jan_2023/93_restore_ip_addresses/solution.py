from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        seq = []

        if len(s) < 4:
            return []

        def backtrack(idx):
            if len(seq) > 4:
                return

            if idx == len(s):
                if len(seq) == 4:
                    result.append(".".join(seq))
                return

            if seq:
                last = seq[-1]
                num_str = last + s[idx]

                if not num_str.startswith("0") and 0 <= int(num_str) <= 255:
                    seq[-1] = num_str
                    backtrack(idx + 1)
                    seq[-1] = last

            seq.append(s[idx])
            backtrack(idx + 1)
            seq.pop()

        backtrack(0)

        return result
