"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hashmap to map the oldNode --> newNode
        # return hashmap[node]

        # recursive dfs function that start from copying
        # node and recursively extend to its neighbours
        # make sure that we are not copying oldNodes as the
        # neighbours of the newNodes

        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            if oldToNew.get(node):
                return oldToNew.get(node)
            
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nb in node.neighbors:
                newNode.neighbors.append(dfs(nb))

            return newNode

        return dfs(node)
        