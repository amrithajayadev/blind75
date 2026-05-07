class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n1 = len(s)
        n2 = len(t)
        sm = Counter(s)

        while i < n1 and j < n2:
            if s[i] == t[j]:
                i += 1
                j += 1
                # sm[s[i]] -= 1
            else:
                j += 1
        if i != n1:
            return False
        else:
            return True
            
        