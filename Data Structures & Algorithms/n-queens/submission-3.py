class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def func(board, r, c):
            if r >= n:
                out.append(board.copy())
                return True
                
            if r < 0 or r >= n or c < 0 or c >= n:
                return False

            for i in range(n):
                if i in cols or r + i in diag1 or r - i in diag2:
                    continue
                diag1.add(r + i)
                diag2.add(r - i)
                cols.add(i)
                board.append(("." * i) + "Q" + ("." * (n - i - 1)))

                func(board, r + 1, i)

                board.pop()
                diag1.remove(r + i)
                diag2.remove(r - i)
                cols.remove(i)

        func([], 0, 0)
        return out