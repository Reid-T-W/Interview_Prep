#!/bin/python3
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """"
        Given a tree, print out the node valus in level
        order traversal
        Args:
            root: TreeNode - root to be traversed
        Returns:
            List[List[int]] - results of traversal
        """
        queue = deque()
        visited = []
        if root:
            queue.append([root])

        while queue:
            visted_append = []
            queue_append = []
            items = queue.popleft()
            for item in items:
                if item:
                    visted_append.append(item.val)
                    queue_append.append(item.left)
                    queue_append.append(item.right)
            if visted_append:
                visited.append(visted_append)
            if queue_append:
                queue.append(queue_append)
        return visited
