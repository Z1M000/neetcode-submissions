class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # all nodes are interconnected. so if we do a dfs, should visit n nodes
        # dfs and check for cycles

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(prev, node):
            if node in visited:
                return False

            visited.add(node)
            
            for nb in graph[node]:
                if nb != prev and dfs(node, nb) == False:
                    return False
            
            return True
        
        return dfs(-1, 0) and len(visited) == n
        
        