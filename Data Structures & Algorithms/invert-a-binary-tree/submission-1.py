# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion
        # base case: leaf node --> return
        # internal node:
        # exchange left and right and recur(left) and recur(right), then return

        def recur(node):
            if not node.left and not node.right:
                return
            
            if not node.left:
                node.left = node.right
                node.right = None
                recur(node.left)
                return
            
            if not node.right:
                node.right = node.left
                node.left = None
                recur(node.right)
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            recur(node.left)
            recur(node.right)
            return
        
        if not root:
            return None

        recur(root)
        return root
        