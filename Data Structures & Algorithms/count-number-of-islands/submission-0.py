class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate thru the grid, if encounter 1, increase the result by 1 and 
        # expand and mark its neighbour in a seperate boolean grid
        # as visited until it all water, and move on and find another unvisited 1 and repeat

        # expand/dfs: find its up, down, left, right neighbour
        # edge case: the item is on the edge, so may not have all neighbours
        # if they are 1 push them to stack
        # end condition of the while loop is the stack is empty

        res = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]



        def expandIsland(rowNum, colNum):
            stack = [(rowNum, colNum)] # list of tuple
            visited[rowNum][colNum] = True
            # count = 0
            while stack:
                # count += 1
                # if count == 30:
                #     return
                cur = stack.pop()
                r, c = cur
                # print(f"cur cell is gird [{r}][{c}]: {grid[r][c]}")
                
                up = (r - 1, c)
                down = (r + 1, c)
                left = (r, c - 1)
                right = (r, c + 1)
                potentialNeighbours = [up, down, left, right]

                for p in potentialNeighbours:
                    # print("  ", p)
                    pr, pc = p
                    if ((0 <= pr < row and 0 <= pc < col)) and visited[pr][pc] == False and grid[pr][pc] == "1":
                        stack.append(p)
                        # print(f"   appended grid [{pr}][{pc}]")
                        visited[pr][pc] = True

            
        

        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == "1" and visited[r][c] == False:
                    # print(f"gird [{r}][{c}] is 1!")
                    res += 1
                    expandIsland(r, c)

        return res



        