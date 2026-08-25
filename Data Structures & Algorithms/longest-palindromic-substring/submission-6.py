class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0, 0
        maxLen = 0

        for i in range(len(s)):
            x = 0
            while i - x >= 0 and i + x < len(s):
                if s[i-x] == s[i+x]:
                    if (i+x) - (i-x) + 1 > maxLen:
                        maxLen = (i+x) - (i-x) + 1
                        start, end = i-x, i+x
                else:
                    break
                x += 1
                
        for i in range(len(s)):
            x = 0
            while i - x >= 0 and i + x + 1 < len(s):
                if s[i-x] == s[i+1+x]:
                    if (i+x+1) - (i-x) + 1 > maxLen:
                        maxLen = (i+x+1) - (i-x) + 1
                        start, end = i-x, i+x+1
                else:
                    break
                x += 1

        return s[start:end+1]      