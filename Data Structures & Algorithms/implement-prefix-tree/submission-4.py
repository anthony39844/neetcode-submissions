class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        child = self.root
        for i in word:
            if i not in child:
                child[i] = {}
            child = child[i]
        child["end"] = True

    def search(self, word: str) -> bool:
        child = self.root
        for i in word:
            if i in child:
                child = child[i]
            else:
                return False

        if "end" in child and child["end"]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        child = self.root
        for i in prefix:
            if i in child:
                child = child[i]
            else:
                return False
        
        return True