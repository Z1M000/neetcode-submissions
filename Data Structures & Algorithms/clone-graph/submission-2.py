"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old2new = {}
        def recur(node):
            if node in old2new:
                return old2new[node]
            
            newNode = Node(node.val)
            old2new[node] = newNode
            for nb in node.neighbors:
                newNode.neighbors.append(recur(nb))
            
            return newNode
        
        res = recur(node)
        return res
            