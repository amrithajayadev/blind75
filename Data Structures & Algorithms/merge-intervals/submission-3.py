class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for interval in intervals:
            if stack and stack[-1][0] <= interval[0] <= stack[-1][1]:
                stack[-1][0] = min(stack[-1][0],interval[0])
                stack[-1][1] = max(stack[-1][1],interval[1])
            else:
                stack.append(interval)
        return stack
        