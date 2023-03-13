import random
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self._arr = self._populate_arr(head)

    def getRandom(self) -> int:
        idx = random.randint(0, len(self._arr) - 1)
        return self._arr[idx].val

    def _populate_arr(self, head: Optional[ListNode]) -> List[ListNode]:
        arr = []
        node = head

        while node:
            arr.append(node)
            node = node.next

        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
