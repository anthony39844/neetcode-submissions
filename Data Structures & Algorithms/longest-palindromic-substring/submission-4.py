class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        start, end = 0, 0

        for m in range(len(s)):
            i = 0
            while m - i >= 0 and m + i < len(s):
                if s[m-i] == s[m+i]:
                    if (m+i) - (m-i) + 1 > maxLen:
                        maxLen = (m+i) - (m-i) + 1
                        start, end = m-i, m+i
                else:
                    break
                i += 1

        for m in range(1, len(s)):
            i = 0
            while m - 1 - i >= 0 and m + i < len(s):
                if s[m-1-i] == s[m+i]:
                    if (m+i) - (m-1-i) + 1 > maxLen:
                        maxLen = (m+i) - (m-1-i) + 1
                        start, end = m-1-i, m+i
                else:
                    break
                i += 1
        return s[start:end+1]

