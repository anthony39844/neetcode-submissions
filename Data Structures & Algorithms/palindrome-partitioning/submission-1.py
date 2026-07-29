class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def func(arr, idx):
            if idx == len(s):
                out.append(arr.copy())
            
            for i in range(idx, len(s)):
                
                st = s[idx:i + 1]
                if st == st[::-1]:
                    arr.append(st)
                    func(arr, i + 1)
                    arr.pop()
        
        func([], 0)
        return out