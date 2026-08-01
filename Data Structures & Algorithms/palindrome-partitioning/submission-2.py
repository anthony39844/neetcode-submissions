class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def dfs(arr, idx):
            if idx == len(s):
                out.append(arr.copy())
                return
            
            for i in range(idx, len(s)):
                st = s[idx:i + 1]
                if st == st[::-1]:
                    arr.append(st)
                    dfs(arr, i + 1)
                    arr.pop()
            
        dfs([], 0)
        return out