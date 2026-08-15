class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # the number of edges of a tree + 1 = the number of nodes
        ne = len(edges)
        if ne+1 != n: return False

        # hashmap called graph (num, nbs)
        # set called visited to record its "ancestors"
        # dfs(num):
        # if num is in visited: return False
        # iterate thru its neighbours
        # if dfs(nb) == False: return False
        # remove num from visited
        # return True

        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # print(graph)

        def dfs(num, prev):
            if num in visited: return False
            # print("checking", num)
            visited.add(num)
            for nb in graph[num]:
                if nb != prev and dfs(nb, num) == False: return False
            
            
            return True
        
        return dfs(0, -1) and len(visited) == n

        # return dfs(0)