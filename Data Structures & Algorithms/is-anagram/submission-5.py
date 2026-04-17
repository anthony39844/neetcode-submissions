class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1

        d2 = {}
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        return d == d2
             