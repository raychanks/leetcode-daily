from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        virtual_head = ListNode(0, head)
        node = virtual_head
        n1 = node.next
        n2 = n1.next

        while n1 and n1.next:
            node.next = n2
            n1.next = n2.next
            n2.next = n1
            node = n1
            n1 = node.next
            n2 = n1.next

        return virtual_head.next
