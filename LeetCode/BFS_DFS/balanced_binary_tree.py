# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left_height = 0
        right_height = 0
        if not root:
            return 1
        left_height += self.isBalanced(root.left)
        if left_height == False:
            return False
        right_height += self.isBalanced(root.right)
        if right_height == False:
            return False
        if abs(left_height - right_height) > 1:
            return False 
        return max(right_height, left_height) + 1
