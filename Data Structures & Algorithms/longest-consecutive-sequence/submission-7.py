class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Create a set for looking up elements in O(1) time
        start a streak from a number if num-1 is not in seen set
        max_streak
        while processing a num, start checking if num + 1 in present in the set
        """
        max_streak = 0
        num_set = set(nums)
        for n in num_set:
            streak = 1
            if n-1 in num_set:
                continue
            while n+1 in num_set:
                streak += 1
                n = n+1
            max_streak = max(max_streak, streak)
        return max_streak