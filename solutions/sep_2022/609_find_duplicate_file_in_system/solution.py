import re
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)

        for path in paths:
            root, *files = path.split(" ")
            for file in files:
                result = re.search(r"(?P<filename>.*)\((?P<content>.*)\)$", file)
                full_path = f"{root}/{result.group('filename')}"
                content = result.group("content")
                content_to_path[content].append(full_path)

        return [value for value in content_to_path.values() if len(value) > 1]
