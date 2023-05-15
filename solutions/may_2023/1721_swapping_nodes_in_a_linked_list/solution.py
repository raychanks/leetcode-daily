from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next

        node = head
        for _ in range(k - 1):
            node = node.next

        tmp = slow.val
        slow.val = node.val
        node.val = tmp

        return head
