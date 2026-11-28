"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True
        
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            x = intervals[i-1]
            y = intervals[i]

            if x.end > y.start:
                return False
        
        return True