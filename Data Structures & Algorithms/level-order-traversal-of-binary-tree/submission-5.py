# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        curLevel = collections.deque()
        curLevel.append(root)
        nextLevel = collections.deque()

        while curLevel:
            vals = [n.val for n in curLevel]
            res.append(vals)

            while curLevel:
                node = curLevel.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                
            curLevel = nextLevel
            nextLevel = collections.deque()
        
        return res
        