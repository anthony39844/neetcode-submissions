class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def func(x, y, idx):
            if idx == len(word):
                return True
            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0:
                return False
            if board[x][y] != word[idx]:
                return False

            temp = board[x][y]
            board[x][y] = "#"
            for i, j in directions:
                if func(x + i, y + j, idx + 1):
                    return True
            board[x][y] = temp
            

        for i in range(len(board)):
            for j in range(len(board[i])):
                if func(i, j, 0):
                    return True
        
        return False