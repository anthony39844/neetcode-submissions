class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for m in range(len(s)):
            i = 0
            while m - i >= 0 and m + i < len(s):
                if s[m-i] == s[m+i]:
                    count += 1
                else:
                    break
                i += 1

        for m in range(1, len(s)):
            i = 0
            while m - 1 - i >= 0 and m + i < len(s):
                if s[m-1-i] == s[m+i]:
                    count += 1
                else:
                    break
                i += 1
        return count