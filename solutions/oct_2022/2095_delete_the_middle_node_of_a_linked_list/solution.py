from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        vnode = ListNode(0, head)
        leader = head

        while leader and leader.next:
            leader = leader.next
            if leader:
                leader = leader.next
                vnode = vnode.next

        vnode.next = vnode.next.next

        return head
