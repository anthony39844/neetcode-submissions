class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        
        out = []
        for i in d.values():
            out.append(i)
        return out