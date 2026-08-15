class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False



class PrefixTree:

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            # print("inserting", w)
            if w not in cur.children:
                cur.children[w] = TrieNode()
            
            cur = cur.children[w]
        
        cur.end = True
        # print("finished inserting")


    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            # print("inserting", w)
            if w not in cur.children:
                return False
            
            cur = cur.children[w]
        
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            # print("inserting", w)
            if w not in cur.children:
                return False
            
            cur = cur.children[w]
        
        return True
        
        