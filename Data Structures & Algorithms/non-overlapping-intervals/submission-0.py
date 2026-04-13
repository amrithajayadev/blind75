class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        res = 0
        for interval in intervals:
            if stack and stack[-1][1] > interval[0]:
                res += 1
                stack[-1][1] = min(stack[-1][1], interval[1])
                stack[-1][0] = min(stack[-1][0], interval[0])
            else:
                stack.append(interval)
        return res
        