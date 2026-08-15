class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create an array of the freq count of letters
        # use that array as the key for the hashmap
        def getKey(s):
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            return tuple(arr)

        group = {}
        for s in strs:
            k = getKey(s)
            if k not in group:
                group[k] = [s]
            else:
                group[k].append(s)
        
        return list(group.values())


        