from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_num_devices = 0
        beam_count = 0

        for row in bank:
            cur_num_devices = row.count("1")
            if not cur_num_devices:
                continue

            beam_count += prev_num_devices * cur_num_devices
            prev_num_devices = cur_num_devices

        return beam_count
