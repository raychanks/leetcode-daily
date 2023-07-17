from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def get_stack(head):
            node = head
            stack = []

            while node:
                stack.append(node.val)
                node = node.next

            return stack

        stack1, stack2 = get_stack(l1), get_stack(l2)
        result = None
        carry = 0

        while stack1 or stack2:
            val1, val2 = 0, 0
            if stack1:
                val1 += stack1.pop()
            if stack2:
                val2 += stack2.pop()

            node_sum = val1 + val2 + carry
            carry = node_sum // 10
            node_sum %= 10

            node = ListNode(node_sum, result)
            result = node

        if carry:
            node = ListNode(carry, result)
            result = node

        return result
