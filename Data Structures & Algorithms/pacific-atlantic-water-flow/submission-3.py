class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or not(r in range(ROW) and c in range(COL)) or heights[r][c] < prevHeight):
                return
        
            visit.add((r, c))
            for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r+d1, c+d2, visit, heights[r][c])

        for c in range(COL):
            dfs(0, c, pac, -1)
            dfs(ROW-1, c, atl, -1)

        for r in range(ROW):
            dfs(r, 0, pac, -1)
            dfs(r, COL-1, atl, -1)
        
        return(list(pac & atl))
        