class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Create a new output list.
        Add all the intervals lesser than new interval.
        - the ends should be smaller than the newInterval[start]
        Add the newInterval or merge with the last.
        Add all intervals greater than the newInterval[end]

        What if the newInterval is at the beginning ?
        """
        output = []
        n = len(intervals)-1
        i = 0

        while i <= n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        while i <= n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        output.append(newInterval)
        
        # if newInterval[0] > output[-1][1]:
        #     output.append(newInterval)
        
        while i <= n:
            output.append(intervals[i])
            i+=1
        return output

        

        