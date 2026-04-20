class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1 = {}
        d2 = {}
        for i in range(26):
            d1[chr(i + ord('a'))] = 0
            d2[chr(i + ord('a'))] = 0
        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if d1[chr(i + ord('a'))] == d2[chr(i + ord('a'))] else 0

        l = 0
        print(matches)
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            d2[s2[r]] += 1
            d2[s2[l]] -= 1
            if d2[s2[r]] == d1[s2[r]]:
                matches += 1
            elif d2[s2[r]] - 1 == d1[s2[r]]:
                matches -= 1
            if d2[s2[l]] == d1[s2[l]]:
                matches += 1
            elif d2[s2[l]] + 1 == d2[s2[l]]:
                matches -= 1
            
            l += 1
        return matches == 26
            
