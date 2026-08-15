# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use two queues curLevel and nextLevel
        # add curLevel's value to res
        # dequeue from curLevel
        # add the left node into the nextLevel if it exists
        # add the right node into the nextLevel if it exists
        # curLevel = nextLevel

        # edge case: root is None
        if root is None:
            return []
        
        res = []
        curLevel = deque([root])
        nextLevel = deque()
        # v = [n.val for n in curLevel]
        # print(v)

        while curLevel:
            values = [n.val for n in curLevel]
            res.append(values)
            while curLevel:
                x = curLevel.popleft()
                # print("x:", x.val)
                if x.left:
                    nextLevel.append(x.left)
                    # print("added", x.left.val, "into nextLevel")
                if x.right:
                    nextLevel.append(x.right)
                    # print("added", x.right.val, "into nextLevel")
            curLevel = nextLevel
            nextLevel = deque()
        
        return res









        