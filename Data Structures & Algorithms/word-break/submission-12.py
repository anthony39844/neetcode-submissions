class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= len(s):
                    if s[i:i+len(word)] == word:
                        dp[i] = dp[len(word) + i] or dp[i]
        return dp[0]