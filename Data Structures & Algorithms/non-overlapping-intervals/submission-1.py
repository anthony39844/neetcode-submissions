class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort()
        out = 0
        prev = intervals[0]

        for i in range(1, len(intervals)):
            x = intervals[i]

            if prev[1] > x[0]:
                out += 1
                x = x if min(x[1], prev[1]) == x[1] else prev
            prev = x

        return out