class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for k in range(minLen):
                if w1[k] != w2[k]:
                    graph[w1[k]].add(w2[k])
                    break
        
        visited = set()
        path = set()
        res = ""
        
        def dfs(c):
            nonlocal res
            if c in path:
                return False
            
            if c in visited:
                return True
            
            visited.add(c)
            path.add(c)
            for nb in graph[c]:
                if not dfs(nb):
                    return False

            res = c + res
            path.remove(c)
            return True
        
        for c in graph:
            if c not in visited:
                if not dfs(c):
                    return ""
        
        return res




