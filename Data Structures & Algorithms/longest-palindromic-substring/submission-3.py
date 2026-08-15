class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 1

        def expand(l, r):
            while (0 <= l and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return l+1, r - l - 1

        for i in range(len(s)):
            # print("odd at", i)
            temp, tempLen = expand(i-1, i+1)
            if tempLen > resLen:
                # print("updating")
                resLen = tempLen
                res = temp
            # print(res, resLen)
            
            # print("even at", i)
            temp, tempLen = expand(i, i+1)
            if tempLen > resLen:
                resLen = tempLen
                res = temp
            # print(res, resLen, "\n")
        
        return s[res: res+resLen]

        