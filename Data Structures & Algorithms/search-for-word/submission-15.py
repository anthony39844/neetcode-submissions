class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def func(x, y, idx):
            if board[x][y] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            visited.add((x, y))
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if 0 <= a < len(board) and 0 <= b < len(board[x]) and (a, b) not in visited:
                    if func(a, b, idx + 1):
                        return True
            visited.remove((x, y))
            
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if func(i, j, 0):
                        return True
        
        return False