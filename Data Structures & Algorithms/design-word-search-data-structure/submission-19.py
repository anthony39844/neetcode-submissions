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
            if idx == len(word):
                if "#" in trie:
                    return True
                else:
                    return False
            if word[idx] == ".":
                for char in trie:
                    if char != "#" and dfs(idx + 1, trie[char]):
                        return True
                return False
            else:
                if word[idx] in trie:
                    trie = trie[word[idx]]
                    if dfs(idx + 1, trie):
                        return True
                return False


        return dfs(0, cur)