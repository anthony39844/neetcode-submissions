class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque()

        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "#"
            if board[i][n-1] == "O":
                q.append((i, n-1))
                board[i][n-1] = "#"
        for j in range(n):
            if board[0][j] == "O":
                q.append((0, j))
                board[0][j] = "#"
            if board[m-1][j] == "O":
                q.append((m-1, j))
                board[m-1][j] = "#"
        print(q)
        while q:
            x, y = q.popleft()

            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == "O":
                    board[a][b] = "#"
                    q.append((a, b))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"