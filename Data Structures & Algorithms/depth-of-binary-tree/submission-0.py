# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recur(node, d):
            if not node:
                return d
            return max(recur(node.left, d+1), recur(node.right, d+1))
        
        return recur(root, 0)
            