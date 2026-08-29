class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def dfs(idx, arr):
            print(idx)
            if idx >= len(s):
                out.append(arr.copy())
                return
            
            for i in range(idx, len(s)):
                x = s[idx:i+1]
                if x == x[::-1]:
                    arr.append(s[idx:i+1])
                    dfs(i + 1, arr)
                    arr.pop()
        
        dfs(0, [])
        return out