#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    temp = root.right
    root.right = root.left
    root.left = temp
    invertTree(root.left)
    invertTree(root.right)
    return root

