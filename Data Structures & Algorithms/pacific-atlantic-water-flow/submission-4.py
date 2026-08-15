class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        p, a = set(), set()

        def recur(r, c, visited, prevHeight):
            if (r in range(ROW) and c in range(COL) 
                and (r, c) not in visited 
                and heights[r][c] >= prevHeight
                ):
                visited.add((r, c))
                for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    recur(r+d1, c+d2, visited, heights[r][c])
        
        for c in range(COL):
            recur(0, c, p, -1)
            recur(ROW-1, c, a, -1)

        for r in range(ROW):
            recur(r, 0, p, -1)
            recur(r, COL-1, a, -1)
        
        return(list(p & a))
        
        