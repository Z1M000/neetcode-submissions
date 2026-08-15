class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, ans = 0, 0, 0, 0
        seen = set()

        while right < len(s):
            char = s[right]
            # print("char", char)
            # print("cur window:", s[left: right+1])

            if char not in seen:
                seen.add(char)
                length += 1
            else:
                # move the left pointer to the first
                # char != char pass the existing char
                # print("cutting the left window")
                while char in seen:
                    # print("- cutting:", s[left])
                    seen.remove(s[left])
                    left += 1
                
                seen.add(char)
                length = right - left + 1
                # print("window after cutting:", s[left: right+1])
            
            ans = max(ans, length)
            right += 1
            # print()

        return ans
                
        