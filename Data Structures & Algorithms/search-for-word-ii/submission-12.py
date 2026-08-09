class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        out = []

        for word in words:
            cur = trie
            for i in word:
                if i not in cur:
                    cur[i] = {}
                cur = cur[i]
            cur["end"] = word

        def dfs(cur, i, j):
            char = board[i][j]
            level = cur[char]
            
            if "end" in level:
                out.append(level["end"])
                del level["end"]
            
            temp, board[i][j] = board[i][j], "#"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(board) and 0 <= b < len(board[0]):
                    c = board[a][b]
                    if c in level:
                        dfs(level, a, b)
            board[i][j] = temp

            if not level:
                del cur[char]

        for i in range(len(board)):
            for j in range(len(board[i])):
                cur = trie
                if board[i][j] in cur:
                    dfs(cur, i, j)
        
        return out
