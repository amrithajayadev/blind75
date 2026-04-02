class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def most_freq_char(hm):
            max_freq = 0
            for k, v in hm.items():
                if v > max_freq:
                    max_freq = v
                    max_k = k
            return max_freq

        i = 0
        j = 0
        n = len(s)
        curr_len = 0
        max_len = 0
        hm = {chr(ch): 0 for ch in range(ord('A'), ord('Z')+1)}
        while j < n:
            hm[s[j]] += 1
            curr_len = j-i+1
            # windowLen - freq of char appearing max num of times 
            # if < k : expand the window else, shrink from left.
            if curr_len - most_freq_char(hm) > k:
                hm[s[i]] -= 1
                i += 1
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len
        
            
            

                
                
                

        