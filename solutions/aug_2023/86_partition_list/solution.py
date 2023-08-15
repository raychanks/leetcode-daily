from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        small_list = ListNode()
        large_list = ListNode()

        curr = head
        curr_small, curr_large = small_list, large_list

        while curr:
            if curr.val < x:
                curr_small.next = curr
                curr_small = curr_small.next
            else:
                curr_large.next = curr
                curr_large = curr_large.next

            curr = curr.next

        curr_small.next = large_list.next
        curr_large.next = None

        return small_list.next
