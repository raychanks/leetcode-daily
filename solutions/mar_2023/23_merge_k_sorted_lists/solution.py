# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        tmp_node = ListNode()
        cur_node = tmp_node

        for i, node in enumerate(lists):
            if node is None:
                continue

            heapq.heappush(heap, (node.val, i))
            lists[i] = node.next

        while heap:
            val, idx = heapq.heappop(heap)
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return tmp_node.next
