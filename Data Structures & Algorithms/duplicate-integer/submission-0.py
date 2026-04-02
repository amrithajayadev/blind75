class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # has duplicate if the length is not equal
        # O(n) + O(n) + O(1) -> time complexity
        # O(n) ~ space complexity
        return len(nums) != len(set(nums))
        