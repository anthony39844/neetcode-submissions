class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        
        cur["end"] = True

    def search(self, word: str) -> bool:
        cur = self.trie

        def dfs(cur, idx):
            for i in range(idx, len(word)):
                w = word[i]
                if w == ".":
                    for char in cur.keys():
                        if char != "end" and dfs(cur[char], i + 1):
                            return True
                    return False
                else:
                    if w in cur:
                        cur = cur[w]
                    else:
                        return False
                        
            if "end" in cur and cur["end"]:
                return True
            return False

        return dfs(cur, 0)
