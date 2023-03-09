from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow, fast = head.next, head.next.next

        while fast is not None and slow != fast:
            slow = slow.next
            fast = fast.next

            if fast is None:
                return None

            fast = fast.next

        if fast is None:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
