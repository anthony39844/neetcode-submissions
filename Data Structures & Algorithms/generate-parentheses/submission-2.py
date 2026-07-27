class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def func(s, o, c):
            if len(s) == n * 2:
                out.append(s)
                return
            
            if o < n:
                func(s + "(", o + 1, c)
            
            if c < o:
                func(s + ")", o, c + 1)
            
        func("", 0, 0)
        return out