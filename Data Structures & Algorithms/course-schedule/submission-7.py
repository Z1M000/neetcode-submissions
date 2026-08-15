class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # an adj list to store course and its prerequisite
        
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True

            visited.add(course)

            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
            
        
        return True


            

        