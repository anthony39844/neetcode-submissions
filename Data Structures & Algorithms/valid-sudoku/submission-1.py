class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        # rows
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in s and board[i][j] != ".":
                    return False
                s.add(board[i][j])
            s.clear()
        
        # columns
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] in s and board[j][i] != ".":
                    return False
                s.add(board[j][i])
            s.clear()

        # 3x3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] in s and board[i + x][j + y] != ".":
                            return False
                        s.add(board[i + x][j + y])
                s.clear()
        
        return True