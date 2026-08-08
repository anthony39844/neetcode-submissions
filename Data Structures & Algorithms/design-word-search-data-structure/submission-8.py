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
        
        def dfs(idx, trie):
            cur = trie
            for i in range(idx, (len(word))): 
                if word[i] == ".":
                    for char in cur.keys():
                        if char != "end" and dfs(i + 1, cur[char]):
                            return True
                    return False
                else:
                    if word[i] in cur:
                        cur = cur[word[i]]
                    else:
                        return False
            if "end" in cur and cur["end"]:
                return True
            return False

        return dfs(0, self.root)
