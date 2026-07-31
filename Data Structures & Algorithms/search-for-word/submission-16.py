class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = Counter(char for row in board for char in row)
        y = Counter(word)
        for char, count in y.items():
            if x[char] < count:
                return False

        visited = set()

        def func(x, y, idx):
            if idx == len(word):
                return True

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            
            if board[x][y] != word[idx]:
                return False

            temp = board[x][y]
            board[x][y] = "#"
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if func(a, b, idx + 1):
                    return True
            board[x][y] = temp
            
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if func(i, j, 0):
                        return True
        
        return False