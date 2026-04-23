class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s
        
        d1 = {}
        d2 = {}
        # build dicts, d1 = baseline, d2 = current window
        for i in range(len(t)):
            d1[t[i]] = d1.get(t[i], 0) + 1
            d2[t[i]] = 0

        matches = 0     
        out = ""
        l, r = 0, 0
        while l < len(s) and s[l] not in t:
            l += 1


        while r < len(s):
            if s[r] in t:
                d2[s[r]] += 1
                if d2[s[r]] == d1[s[r]]:
                    matches += 1

            while matches == len(d1.keys()):
                print(l, r)
                out = s[l:r + 1] if len(s[l:r + 1]) < len(out) or out == "" else out
                d2[s[l]] -= 1
                if d2[s[l]] < d1[s[l]]:
                    matches -= 1
                l += 1
                while l < len(s) and s[l] not in t:
                    l += 1
            
            r += 1
  
        return out

