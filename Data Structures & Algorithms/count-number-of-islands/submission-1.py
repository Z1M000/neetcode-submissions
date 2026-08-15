class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        ans = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def expandIsland(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for d1, d2 in dirs:
                    newR, newC = r+d1,c+d2
                    if 0<=newR<ROW and 0<=newC<COL and grid[newR][newC]=="1":
                        stack.append((newR, newC))
                    grid[r][c] = "0"
            
            # for row in grid:
            #     for item in row:
            #         print(item, end=" ")
            #     print()
            

                  
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    ans += 1
                    expandIsland(r, c)
                    # print("expanding island")
        
        return ans

        