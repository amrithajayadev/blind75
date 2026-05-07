class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split()
        return len(lst[-1])
        