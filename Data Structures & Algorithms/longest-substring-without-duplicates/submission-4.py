class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = 0
        seen = {}
        for right, ch in enumerate(s):
            if ch in seen and seen[ch]>= left:
                left = seen[ch] + 1
            
            seen[ch] = right
            maxlen = max(maxlen, right-left + 1)
        return maxlen


