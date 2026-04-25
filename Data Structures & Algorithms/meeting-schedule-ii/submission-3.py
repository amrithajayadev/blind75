"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        n = len(intervals)
        i = 0
        j = 0
        count = 0
        max_count = 0
        while i<n and j < n:
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_count = max(max_count, count)
        
        return max_count


        


        