class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque()

        for i in range(m):
            for j in (0, n-1):
                if board[i][j] == "O":
                    q.append((i, j))
                    board[i][j] = "#"
        for j in range(n):
            for i in (0, m-1):
                if board[i][j] == "O":
                    q.append((i, j))
                    board[i][j] = "#"

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