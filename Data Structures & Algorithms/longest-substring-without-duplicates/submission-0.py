class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        st1 = set()
        curr_len = 0
        j = 0
        i = 0
        while i < n and j < n:
            if s[j] not in st1:
                st1.add(s[j])
                curr_len += 1
                print(f"Adding {s[j]} from the position:{j}")   
            else:
                while i < j and s[j] in st1: 
                    print(f"Removing {s[i]} from the position:{i}")   
                    st1.remove(s[i])
                    curr_len -= 1
                    i += 1
                j -= 1
                    
            max_len = max(max_len, curr_len)
            j += 1
        print(max_len)
        return max_len


        