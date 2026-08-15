class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap called preMap to store the graph (course, prereqs)
        # set called visited to store visited chain / ancestors
        # recur dfs(course)
        # if course in visited: return false
        # if course's prereq is [], return true
        # add course to visited map, dfs its prereqs, if any prereq return false, return false
        # change its prereq to []
        # remove course from visited map

        # run dfs on every course just in case the graph is not connected

        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # print(preMap)

        visited = set()

        def dfs(course):
            if course in visited: return False
            if preMap[course] == []: return True

            visited.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False: return False
            
            # preMap[course] = []
            visited.remove(course)
        
        for i in range(numCourses):
            if dfs(i) == False: return False

        return True
        