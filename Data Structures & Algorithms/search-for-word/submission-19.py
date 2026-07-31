class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):

            if idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(i + x, j + y, idx + 1):
                    return True
            board[i][j] = temp


        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False