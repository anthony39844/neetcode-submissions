class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]

        cur["#"] = True

    def search(self, word: str) -> bool:
        cur = self.trie

        def dfs(idx, trie):
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for char, child in trie.items():
                        if char != "#" and dfs(i + 1, child):
                            return True
                    return False
                
                if c not in trie:
                    return False
                trie = trie[c]
            return "#" in trie
                

        return dfs(0, cur)