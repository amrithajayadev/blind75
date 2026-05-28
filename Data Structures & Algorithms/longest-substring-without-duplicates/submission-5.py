class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        win = set()
        max_len = 0
        while j < n:
            if s[j] not in win:
                win.add(s[j])
                max_len = max(max_len, j-i+1)
            else:
                while i < j and s[j] in win:
                    win.remove(s[i])
                    i += 1
                win.add(s[j])
            j += 1
        return max_len
        
        