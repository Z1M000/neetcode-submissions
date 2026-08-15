class TrieNode:
    def __init__(self, parent: TrieNode, key: str):
        self.parent = parent
        self.key = key
        self.isEnd = False
        self.children = [None for i in range(26)]
    
    def printChildren(self):
        print("   * printing children for", self.key)
        for i in range(26):
            if self.children[i]:
                print("   *", i, self.children[i].key, self.children[i])

class PrefixTree:
    def __init__(self):
        self.root = TrieNode(None, None)
        
    def insert(self, word: str) -> None:
        # )
        # "inserting", word)
        # "- 0", word[0])
        key = word[0]
        keyIndex = ord(key) - ord('a')   
        if not self.root.children[keyIndex]:
            node = TrieNode(self.root, key)
            self.root.children[keyIndex] = node
            # self.root.printChildren()
        else:
            node = self.root.children[keyIndex]
        
        if len(word) == 1:
            node.isEnd = True
        for i in range(1, len(word)):
            # "-", i, word[i])
            k = word[i]
            kIndex = ord(k) - ord('a')
            if not node.children[kIndex]:
                newNode = TrieNode(node, k)
                node.children[kIndex] = newNode
                # node.printChildren()
            else:
                newNode = node.children[kIndex]
            
            if i == len(word) - 1:
                newNode.isEnd = True
                # "finished inserting")
            node = newNode


    def search(self, word: str) -> bool:
        # )
        res = False
        # "searching", word)
        # "- checking 0", word[0])
        key = word[0]
        keyIndex = ord(key) - ord('a')   
        if not self.root.children[keyIndex]:
            return False
        else:
            node = self.root.children[keyIndex]
            if len(word) == 1:
                res = node.isEnd
            # self.root.printChildren()

        for i in range(1, len(word)):
            # "- checking", i, word[i])
            k = word[i]
            kIndex = ord(k) - ord('a')
            # node.printChildren()
            # " 🔍 finding", k, "index", kIndex)
            # # "node.children[keyIndex]:", node.children[keyIndex])
            if not node.children[kIndex]:
                # # " ❌", k, "not found")
                return False
            else:
                # # " ✅", k, "found")
                newNode = node.children[kIndex]

            
            if i == len(word) - 1:
                res = newNode.isEnd
                # # "ran till the end")
            node = newNode 
        
        ## "finished checking")
        return res
        

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        # )
        res = False
        # "searching", word)
        # "- checking 0", word[0])
        key = word[0]
        keyIndex = ord(key) - ord('a')   
        if not self.root.children[keyIndex]:
            return False
        else:
            node = self.root.children[keyIndex]
            if len(word) == 1:
                res = True
            # self.root.printChildren()

        for i in range(1, len(word)):
            # "- checking", i, word[i])
            k = word[i]
            kIndex = ord(k) - ord('a')
            # node.printChildren()
            # " 🔍 finding", k, "index", kIndex)
            # # "node.children[keyIndex]:", node.children[keyIndex])
            if not node.children[kIndex]:
                # " ❌", k, "not found")
                return False
            else:
                # " ✅", k, "found")
                newNode = node.children[kIndex]

            
            if i == len(word) - 1:
                res = True
                # "ran till the end")
            node = newNode 
        
        # "finished checking\n")
        return res


        
        