from collections import deque
from typing import List
from urllib.parse import urlparse

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser:
    def getUrls(self, url) -> List[str]:
        """
        :type url: str
        :rtype List[str]
        """
        ...


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        seen = set()
        queue = deque([startUrl])
        result = []

        while queue:
            url = queue.popleft()

            if url in seen:
                continue

            seen.add(url)
            result.append(url)

            for u in htmlParser.getUrls(url):
                if u in seen or not self._is_same_hostname(u, startUrl):
                    continue

                queue.append(u)

        return result

    @staticmethod
    def _is_same_hostname(url1: str, url2: str) -> bool:
        return urlparse(url1).hostname == urlparse(url2).hostname
