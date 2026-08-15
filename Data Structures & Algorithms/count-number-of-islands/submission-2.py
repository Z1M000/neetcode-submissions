class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def expandIsland(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                grid[r][c] = "0"
                for d1, d2 in dirs:
                    newR, newC = r+d1, c+d2
                    if newR in range(ROW) and newC in range(COL) and grid[newR][newC] == "1":
                        stack.append((newR, newC))
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    expandIsland(r, c)
        
        return res
