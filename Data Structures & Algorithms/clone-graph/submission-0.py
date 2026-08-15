"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # oldToNew: (originalNode, copy)
        # copy = Node(node.val) --> an address to the node
        # store the copy into the hashmap
        # recursive dfs to clone their neighbors before appending them into the 
        # neighbors of the copy

        if node is None:
            return None

        oldToNew = {}

        def clone(node):
            if oldToNew.get(node):
                return oldToNew.get(node)
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            
            return copy
        
        res = clone(node)
        return res

        