class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(r, arr):
            if r >= n:
                out.append(arr.copy())
                return
            
            for c in range(n):
                if r-c not in diag1 and r+c not in diag2 and c not in cols:
                    cols.add(c)
                    diag1.add(r-c)
                    diag2.add(r+c)
                    board = ("." * c) + "Q" + ("." * (n - c - 1))
                    arr.append(board)
                    dfs(r + 1, arr)
                    arr.pop()
                    cols.remove(c)
                    diag1.remove(r-c)
                    diag2.remove(r+c)
            

        dfs(0, [])
        return out