class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                x = len(word)
                if i+x <= len(s) and dp[x + i] and s[i:i+x] == word:
                    dp[i] = True
                    break
        return dp[0]