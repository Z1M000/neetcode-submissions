# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSubtree(root, subRoot):
            if not subRoot: return True
            if not root: return False

            if isSameTree(root, subRoot):
                return True
            
            return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))

        def isSameTree(s, t):
            if not s and not t:
                return True
            
            if s and t and s.val == t.val:
                return (isSameTree(s.left, t.left) and isSameTree(s.right, t.right))
            
            return False

        
        return isSubtree(root, subRoot)
        