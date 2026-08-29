class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True

            temp, board[i][j] = board[i][j], "#"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == word[idx]:
                    if dfs(a, b, idx + 1):
                        return True
            board[i][j] = temp

            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        
        return False