class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print("s", s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # print('i', i, "j", j)
            # print(s[i: j])
            length = int(s[i: j])
            # print("len", length)
            word = s[j+1: j+length+1]
            # print("word", word)
            res.append(word)
            i = j+length+1
        
        return res
