class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        
        cur["end"] = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for i in word:
            if i in cur:
                cur = cur[i]
            else:
                return False
        
        if "end" in cur and cur["end"]:
            return True
        return False 

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for i in prefix:
            if i in cur:
                cur = cur[i]
            else:
                return False
        
        return True
        