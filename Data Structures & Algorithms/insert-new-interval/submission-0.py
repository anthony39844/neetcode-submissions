class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(intervals)):
            x = intervals[i]
            if newInterval[1] < x[0]: # newInterval is smaller than this interval
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > x[1]: # newInterval is bigger than this interval
                out.append(x)
            else: # newInterval is between intervals
                newInterval = [min(x[0], newInterval[0]), max(x[1], newInterval[1])]

        out.append(newInterval)
        return out