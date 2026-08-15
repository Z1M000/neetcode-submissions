class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # scan thru the grid and find the starting char
        # then explore all 4 directions to find the next char
        # if all 4 directions don't work we find the next starting char
        # directions = [
        #     [1, 0], [-1, 0], [0, -1], [0, 1]
        # ]
        visited = set()
        ROW = len(board)
        COL = len(board[0])

        def recur(i, curR, curC): 
            # compare if word[0] equals board[curR][curC]
            # if not return False
            # if so if i = len(word) - 1, return True
            # else return recur(i+1, updatedR, updatedC) for all four direction
            # using OR

            # print("curR:", curR, "curC:", curC)
            if not (0<=curR<ROW and 0<=curC<COL):
                # print("return False: index not in bound")
                return False
            if (curR, curC) in visited: 
                # print("return False: already visited")
                return False
            if board[curR][curC] != word[i]: 
                # print("return False:", board[curR][curC], "!=", word[i])
                return False

            # print(board[curR][curC], "==", word[i])
            if i == len(word) - 1:
                # print("RETURN TRUE: FOUND THE WORD!!!")
                return True

            visited.add((curR, curC))
            # print("added", (curR, curC), "to visited")
            res = recur(i+1, curR+1, curC) or recur(i+1, curR-1, curC) or recur(i+1, curR, curC+1) or recur(i+1, curR, curC-1)
            visited.remove((curR, curC))
            # print("removed", (curR, curC), "from visited")
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if recur(0, r, c):
                    return True
        
        return False



        


                            

                    


        