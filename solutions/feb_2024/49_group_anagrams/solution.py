from collections import defaultdict
from typing import List


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ",".join(sorted(list(s)))
            groups[key].append(s)

        return list(groups.values())
