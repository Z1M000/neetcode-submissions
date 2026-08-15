class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        
        def recur(i):
    
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = recur(i+1)
            if i < len(s) - 1 and int(s[i: i+2]) <= 26:
                res += recur(i+2)
            
            dp[i] = res
            return res

        return recur(0)
            