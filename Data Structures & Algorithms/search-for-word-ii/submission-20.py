class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        out = []

        for word in words:
            cur = trie
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur["#"] = word
        print(trie)
        def dfs(trie, i, j):
            char = board[i][j]
            if char not in trie:
                return False
            child = trie[char]
            
            if "#" in child:
                out.append(child["#"])
                del child["#"]

            temp, board[i][j] = board[i][j], "#"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] in child:
                    dfs(child, a, b)
            board[i][j] = temp
            if not child:
                del trie[char]


        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    cur = trie
                    dfs(cur, i, j)
        
        return out