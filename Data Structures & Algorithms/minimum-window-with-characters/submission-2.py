class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        window = {}

        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == countT[s[r]]:
                    have += 1
                
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        
        if res == [-1, -1]:
            return ""
        
        l, r = res
        return s[l: r+1]
            