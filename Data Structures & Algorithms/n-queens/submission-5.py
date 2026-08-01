class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        diag1 = set()
        diag2 = set()
        cols = set()

        def dfs(r, arr):
            if r == n:
                out.append(arr.copy())
                return
            
            for c in range(n):
                if r+c in diag1 or r-c in diag2 or c in cols:
                    continue
                diag1.add(r+c)
                diag2.add(r-c)
                cols.add(c)
                arr.append(("." * c) + "Q" + ("." * (n - c - 1)))
                dfs(r + 1, arr)
                arr.pop()
                diag1.remove(r+c)
                diag2.remove(r-c)
                cols.remove(c)

        dfs(0, [])
        return out
