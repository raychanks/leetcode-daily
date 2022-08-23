from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid point
        slow, fast = head, head

        while fast:
            fast = fast.next

            if fast:
                slow = slow.next
                fast = fast.next

        # reverse linked list
        node = slow
        curr = None
        next_node = node.next

        while node:
            node.next = curr
            curr = node
            node = next_node

            if node:
                next_node = node.next

        # start comparison
        from_head = head
        from_tail = curr

        while from_tail:
            if from_tail.val != from_head.val:
                return False
            from_tail = from_tail.next
            from_head = from_head.next

        return True


class SolutionToList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        while head:
            l.append(head.val)
            head = head.next

        left, right = 0, len(l) - 1

        while left < right:
            if l[left] != l[right]:
                return False

            left += 1
            right -= 1

        return True
