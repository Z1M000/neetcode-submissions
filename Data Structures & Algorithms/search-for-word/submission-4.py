class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        
        def recur(i , r, c):
            if i == len(word):
                return True
            
            if not(0<=r<ROW and 0<=c<COL) or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            res = recur(i+1, r+1, c) or recur(i+1, r-1, c) or recur(i+1, r, c+1) or recur(i+1, r, c-1)
            if res:
                return True
            visited.remove((r, c))
            return False
        
        for r in range(ROW):
            for c in range(COL):
                if recur(0, r, c):
                    return True
        
        return False
        