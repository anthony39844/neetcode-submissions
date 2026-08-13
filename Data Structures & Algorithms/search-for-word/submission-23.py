class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(idx, x, y):
            if idx == len(word):
                return True
            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0])):
                return False
            if board[x][y] != word[idx]:
                return False
            
            temp = board[x][y]
            board[x][y] = "#"
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if dfs(idx + 1, a, b):
                    return True
            board[x][y] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        
        return False