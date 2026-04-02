class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer solution
        # keep advancing the second pointer (j)
        # add the chars to a set
        # increment the length of the window.
        # stop the second pointer when a non-unique char is found.
        # update max length with curr window length if higher.
        # advance the i pointer until the same char as j. 
        
        i = 0
        j = 0
        curLen = 0
        maxLen = 0
        n = len(s)
        s1 = set()
        while j < n:
            if s[j] not in s1:
                s1.add(s[j])
                curLen += 1
            else:
                while s1 and s[j] in s1:
                    s1.remove(s[i])
                    i += 1
                s1.add(s[j])
                curLen = j - i + 1
            j += 1
            maxLen = max(maxLen, curLen)
        return maxLen




