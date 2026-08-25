class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0, 0
        maxLen = 0

        def expand(l, r):
            nonlocal maxLen, start, end
            x = 0
            while l - x >= 0 and r + x < len(s):
                if s[l-x] == s[r+x]:
                    if (r+x) - (l-x) > maxLen:
                        maxLen = (r+x) - (l-x)
                        start, end = l-x, r+x
                else: break
                x += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start:end+1]      