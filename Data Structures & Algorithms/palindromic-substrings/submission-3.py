class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 0

        def expand(l, r):
            nonlocal out
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    out += 1
                else:
                    break
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return out