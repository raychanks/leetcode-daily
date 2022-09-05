# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        answer: List[List[int]] = []

        if not root:
            return answer

        queue = [root]
        num_node_in_lv = len(queue)
        num_node_remaining_in_lv = num_node_in_lv
        current_level = []

        while queue:
            node = queue.pop(0)
            current_level.append(node.val)
            num_node_remaining_in_lv -= 1

            if node.children:
                queue.extend(node.children)

            if num_node_remaining_in_lv == 0:
                answer.append(current_level)
                current_level = []
                num_node_in_lv = len(queue)
                num_node_remaining_in_lv = num_node_in_lv

        return answer
