from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            group[sorted_s].append(s)
        return list(group.values())
