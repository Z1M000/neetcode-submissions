class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        minLen = float("inf")
        tmap = {}

        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        have, need = 0, len(tmap)

        # print(tmap)
        # print("have", have, "need", need)
        smap = {}


        for r in range(len(s)):
            # if the window doesn't contain t, increase the right pointer
            # if the window does contain t, increase the left pointer until it doesn't, then we update the res
            # use freq map to check
            # print("s[r]:", s[r])
            if s[r] in tmap:
                smap[s[r]] = 1 + smap.get(s[r], 0)
                if smap[s[r]] == tmap[s[r]]:
                    have += 1
            
            while have == need:
                # print("have == need!")
                if minLen > r - l + 1:
                    # print("updating res")
                    minLen = r - l + 1
                    res = s[l: r+1]
                if s[l] in tmap:
                    smap[s[l]] -= 1
                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1
            
                
    
        return res

                


        