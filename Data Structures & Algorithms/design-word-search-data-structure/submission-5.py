class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur["end"] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
                
            if word[i] == ".":
                for char in cur.keys():
                    w = word[:i] + char + word[i+1:]
                    if self.search(w):
                        return True
                return False
            else:
                if word[i] not in cur:
                    return False
                cur = cur[word[i]]

        if "end" in cur and cur["end"]:
            return True
        return False
