class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        seen = set()

        while right < len(s):
            char = s[right]

            if char not in seen:
                seen.add(char)
            else:
                while char in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(char)
            
            length = right - left + 1
            res = max(res, length)
            right += 1
        
        return res



        