class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def func(s, o, c):
            if len(s) == n * 2:
                out.append(s)
                return
            
            if o < n:
                s += "("
                func(s, o + 1, c)
                s = s[:-1]
            
            if c < o:
                s += ")"
                func(s, o, c + 1)
                s = s[:-1]
            
        func("", 0, 0)
        return out