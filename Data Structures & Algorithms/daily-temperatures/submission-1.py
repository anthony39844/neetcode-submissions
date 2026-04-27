class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        s = []

        for i, t in enumerate(temperatures):
            print(s)
            while s and s[-1][1] < t:
                x = s.pop()
                print(x)
                out[x[0]]= i - x[0]
            s.append([i, t])
        
        return out