class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ss = set()
        d = Counter(s)
        out = []
        size = 0
        for i in s:
            size += 1
            ss.add(i)
            d[i] -= 1
            if d[i] == 0:
                ss.remove(i)
            if not ss:
                out.append(size)
                size = 0
        
        return out
