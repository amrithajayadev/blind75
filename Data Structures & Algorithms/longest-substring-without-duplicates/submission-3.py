class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window problem
        keep all the elements of current window in a hash map
        expand the window until we enounter a char that is already seen
        shrink the window until the repeating char
        """

        n = len(s)
        i = 0
        j = 0
        hm = {}
        max_len = 0
        while j < n:
            if s[j] not in hm:
                hm[s[j]] = 1 + hm.get(s[j],0)
                max_len = max(max_len, j-i+1)
            else:
                while i < j and s[j] in hm:
                    hm.pop(s[i])
                    i += 1
                hm[s[j]] = 1 + hm.get(s[j],0)
            j += 1
        return max_len


