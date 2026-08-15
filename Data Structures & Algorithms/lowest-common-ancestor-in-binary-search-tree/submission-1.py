# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p < node and q > node or the other way, their LCA has to be node
        # if encountered p but not yet q, then return p
        # if encountered q but not yet p, then return q

        # recur(node)
        # if node == p return p
        # if node == q return q
        # if p < node and q > node or the other way, return node
        # if both p and q < node, recur(node.left)
        # if both p and q > node, recur(node.right)

        def recur(node):
            print("node", node.val)
            if node.val == p.val: return p
            if node.val == q.val: return q
            if ((p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val)):
                return node
            if (p.val < node.val and q.val < node.val):
                return recur(node.left)
            if (p.val > node.val and q.val > node.val):
                return recur(node.right)

        print("p", p.val)  
        print("q", q.val)
        return recur(root)
            




        
        