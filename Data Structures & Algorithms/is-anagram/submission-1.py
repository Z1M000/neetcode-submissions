class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash, thash = {}, {}
        for c in s:
            shash[c] = shash[c] + 1 if c in shash else 1 
        
        for c in t:
            thash[c] = thash[c] + 1 if c in thash else 1 

        if shash.keys() != thash.keys():
            return False
        
        for k, v in shash.items():
            if k not in thash or thash[k] != v:
                return False
        
        return True