class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        max_len = 0
        for i, n in enumerate(nums):
            curr_len = 1
            if n-1 in st and n+1 not in st:
                continue
            if n+1 in st:
                while n+1 in st:
                    n += 1
                    curr_len += 1
                # max_len = max(max_len, curr_len)
            max_len = max(max_len, curr_len)
        return max_len
                    