class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        graph = {}

        for c1, c2 in prerequisites:
            if c1 in graph:
                graph[c1].append(c2)
            else:
                graph[c1] = [c2]
        
        # print(graph)

        def recur(c):
            # print("c", c)
            # print("path", path)
            if c in path:
                # print("c in path, returning False")
                return False
            path.add(c)
            visited.add(c)
            if c in graph:
                for nb in graph[c]:
                    if not recur(nb):
                        return False
            path.remove(c)
            graph[c] = []
            return True
        
        for n in range(numCourses):
            # print("\nn", n)
            # print("recur(n)", recur(n))
            if n not in visited and not recur(n):
                # print("n not in visited and not recur(n), returning False")
                return False
        
        return True
        