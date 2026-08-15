class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROW = len(board)
        COL = len(board[0])

        def recur(i, curR, curC): 
            if not (0<=curR<ROW and 0<=curC<COL) or board[curR][curC] != word[i] or (curR, curC) in visited:
                return False
            
            if i == len(word) - 1: return True
            visited.add((curR, curC))
            res = recur(i+1, curR+1, curC) or recur(i+1, curR-1, curC) or recur(i+1, curR, curC+1) or recur(i+1, curR, curC-1)
            visited.remove((curR, curC))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if recur(0, r, c):
                    return True
        
        return False



        


                            

                    


        