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

        visited = set()
        def dfs(cur, i, j):
            char = board[i][j]
            level = cur[char]
            if char in visited:
                return False
            
            if "end" in level:
                out.append(level["end"])
                del level["end"]
            
            visited.add((i, j))
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and (a, b) not in visited:
                    char = board[a][b]
                    if char in level:
                        dfs(level, a, b)
            visited.remove((i, j))

            if not level:
                del cur


        for i in range(len(board)):
            for j in range(len(board[i])):
                cur = trie
                if board[i][j] in cur:
                    dfs(cur, i, j)
        
        return out
                    
                
        

                
