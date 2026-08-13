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
        
        def dfs(x, y, trie):
            char = board[x][y]
            child = trie[char]
            if "end" in child:
                out.append(child["end"])
                del child["end"]
            
            temp, board[x][y] = board[x][y], "#"
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] != "#":
                    if board[a][b] in child:
                        dfs(a, b, child)
            board[x][y] = temp

            if not child:
                del trie[char]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                cur = trie
                if board[i][j] in cur:
                    dfs(i, j, cur)
        
        return out