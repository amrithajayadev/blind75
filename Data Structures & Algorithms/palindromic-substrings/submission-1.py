class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        1. Each single char is a palindrome in itself
        2. For each char, expand left and right to check if a palindrome can be formed
        abbaccaa
        a,b, bb, abba, abba, b, a, c, cc, acca, c,a, a
        """

        subs = []
        n = len(s)
        for i in range(n):
            # odd case
            l, r = i, i
            while l >= 0 and r <= n-1 and s[l]==s[r]:
                print("Odd case", l, r)
                subs.append(s[l:r+1])
                l -= 1
                r += 1
            # even case
            l, r = i, i + 1
            while l >= 0 and r <= n-1 and s[l]==s[r]:
                print("Even case", l, r)
                subs.append(s[l:r+1])
                l -= 1
                r += 1
            print(subs)
        return len(subs)
        
