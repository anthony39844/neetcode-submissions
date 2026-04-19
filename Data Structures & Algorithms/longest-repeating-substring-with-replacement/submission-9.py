class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        d = {}
        l = 0
        maxf = 0
        out = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            maxf = max(maxf, d[s[i]])
            while i - l + 1 - maxf > k:
                d[s[l]] -= 1
                l += 1

            out = max(out, i - l + 1)

        return out