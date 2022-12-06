# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd_head = head
        even_head = head.next
        cur_odd = odd_head
        cur_even = even_head

        while cur_even:
            next_odd = cur_even.next

            if not next_odd:
                break

            cur_odd.next = next_odd
            cur_odd = next_odd

            next_even = cur_odd.next

            cur_even.next = next_even
            cur_even = next_even

        cur_odd.next = even_head

        return odd_head
