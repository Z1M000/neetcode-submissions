class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 1

        def expand(l, r, length):
            while (0 <= l < r and l < r < len(s)):
                # print("l", l, s[l])
                # print("r", r, s[r])
                if s[l] == s[r]:
                    # print("equal")
                    length += 2
                    l -= 1
                    r += 1
                else:
                    break
            
            # print("end")
            return l+1, length

        for i in range(len(s)):
            # print("odd at", i)
            temp, tempLen = expand(i-1, i+1, 1)
            if tempLen > resLen:
                # print("updating")
                resLen = tempLen
                res = temp
            # print(res, resLen)
            
            # print("even at", i)
            temp, tempLen = expand(i, i+1, 0)
            if tempLen > resLen:
                resLen = tempLen
                res = temp
            # print(res, resLen, "\n")
        
        return s[res: res+resLen]

        