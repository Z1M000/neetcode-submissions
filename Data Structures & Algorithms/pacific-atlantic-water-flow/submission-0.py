class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # initialize a pacific stack and atlantic stack
        # initialize a set for unvisited checking
        # initialize two sets to record valid cells
        # for pacific stack, we push first row and first column
        # for each stack, we gonna pop the cell and record it and
        # append all its unvisited and equal or higher neighbours into the stack

        # intersect the set and turn it into a list

        numR = len(heights)
        numC = len(heights[0])

        pstack = [(0, c) for c in range(numC)] + [(r, 0) for r in range(1, numR)]
        astack = [(numR-1, c) for c in range(numC)] + [(r, numC-1) for r in range(0, numR-1)]

        # print(pstack)
        # print(astack)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


        def neighbour(a, b):
            nbs = []
            for d in directions:
                x, y = d
                if 0 <= a+x < numR and 0 <= b+y < numC:
                    nbs.append((a+x, b+y))
            
            return nbs
                

        def dfs(stack):
            # for each stack, we gonna pop the cell and record it and
            # append all its unvisited and equal or higher neighbours into the stack
            visited = set()
            res = set()
            while stack:
                cur = stack.pop()
                r, c = cur
                # print("height", heights[r][c])
                visited.add(cur)
                res.add(cur)
                nbs = neighbour(r, c)
                # print(nbs)
                for nb in nbs:
                    x, y = nb
                    if not nb in visited and heights[x][y] >= heights[r][c]:
                        stack.append(nb)

            return res

        res = dfs(pstack) & dfs(astack)
        # print(res)
        output = []

        for r,c in res:
            output.append([r, c])
        
        return output
        
        
        



        
        