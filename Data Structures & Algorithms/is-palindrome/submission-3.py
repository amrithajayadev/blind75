class Solution:
    def isPalindrome(self, s: str) -> bool:
        an_set = set()
        for ch in range(ord('a'),ord('z')+1):
            an_set.add(chr(ch))
        for ch in range(ord('A'),ord('Z')+1):
            an_set.add(chr(ch))
        for ch in range(0,10):
            an_set.add(str(ch))
        
        start = 0
        end = len(s)-1
        # convert all chars to lowercase 
        s = s.lower()

        while start <= end:
            if s[start] not in an_set:
                print(f"Skipping {s[start]} because s[start]={s[start]}")
                start += 1
                continue
            if s[end] not in an_set:
                print(f"Skipping {s[end]} because s[end]={s[end]}")
                end -= 1
                continue
            if s[start] == s[end]:
                print(f"comparing {s[start]} and {s[end]}")
                start +=1
                end -= 1
            else:
                return False
            
        return True
            

        