class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) * len(board[0]) < len(word):
            return False
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def func(x, y, s):
            print(s)
            if s == word:
                return True
            
            if len(s) < len(word):
                for i, j in directions:
                    a, b = x + i, y + j
                    if (0 <= a < len(board)) and (0 <= b < len(board[0])) and (a, b) not in visited:
                        visited.add((a, b))
                        if func(a, b, s + board[a][b]):
                            return True
                        visited.remove((a, b))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if func(i, j, board[i][j]):
                    return True
        
        return False