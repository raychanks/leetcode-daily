from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        subsequent_mask = 0b11000000
        subsequent_bytes = 0

        for byte in data:
            if subsequent_bytes:
                if byte & subsequent_mask != 0b10000000:
                    return False
                subsequent_bytes -= 1
            else:
                if byte & 0b10000000 == 0b00000000:
                    continue
                elif byte & 0b11100000 == 0b11000000:
                    subsequent_bytes = 1
                elif byte & 0b11110000 == 0b11100000:
                    subsequent_bytes = 2
                elif byte & 0b11111000 == 0b11110000:
                    subsequent_bytes = 3
                else:
                    return False

        return not subsequent_bytes
