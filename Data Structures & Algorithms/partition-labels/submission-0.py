class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ss = set()
        d = Counter(s)
        out = []
        l, r = -1, 0
        while r < len(s):
            if s[r] not in ss:
                ss.add(s[r])
            d[s[r]] -= 1
            if d[s[r]] == 0:
                ss.remove(s[r])
            if len(ss) == 0:
                out.append(r - l)
                l = r
            r += 1
        
        return out
