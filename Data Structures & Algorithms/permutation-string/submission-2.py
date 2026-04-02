class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch in s1:
            s1_map[ch] = 1 + s1_map.get(ch, 0)
        
        k = len(s1) # window length
        N = len(s2)
        i = 0
        j = 0 
        if k > N:
            return False

        while j <= N - k:
            if s2[j] not in s1_map:
                j += 1
            else:
                s2_map = {}
                for i in range(j, j+k):
                    s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)

                if s1_map == s2_map:
                    return True
                j += 1
        return False

        