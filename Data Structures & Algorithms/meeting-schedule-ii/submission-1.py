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

        i = 0
        j = 0
        n = len(intervals)
        res = 0
        max_rooms = 0
        while i < n and j < n:
            if starts[i] < ends[j]:
                res += 1
                i += 1
            elif ends[j] <= starts[i]:
                res -= 1
                j += 1
            max_rooms = max(max_rooms, res)
        return max_rooms

        