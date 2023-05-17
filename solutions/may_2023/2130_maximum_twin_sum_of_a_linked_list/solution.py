from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = []
        current_max = 0

        slow, fast = head, head.next
        while fast:
            sums.append(slow.val)
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        idx = len(sums) - 1
        while slow:
            sums[idx] += slow.val
            current_max = max(current_max, sums[idx])
            slow = slow.next
            idx -= 1

        return current_max
