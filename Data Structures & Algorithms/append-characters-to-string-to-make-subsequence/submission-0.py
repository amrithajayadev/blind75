class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        LCS - longest common subsequence length
        """

        tl = len(t)
        sl = len(s)
        i = 0
        j = 0
        while i < tl and j < sl:
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return tl-i

    
        