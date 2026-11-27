class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            x = out[-1]
            y = intervals[i]

            if x[1] < y[0]:
                out.append(y)
            elif x[1] >= y[0]:
                out[-1] = [min(x[0], y[0]), max(x[1], y[1])]
        
        return out

