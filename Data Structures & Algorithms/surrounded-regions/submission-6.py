class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j):
            board[i][j] = "#"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == "O":
                    dfs(a, b)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        