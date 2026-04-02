class Solution:

    def longestPalindrome(self, s: str) -> str:

        odd_res = ""
        even_res = ""
        resLen = 0
        maxLen = 0
        n = len(s)
        for i in range(len(s)):
            # odd case
            j = i
            k = i
            while j >= 0 and k < n and s[j] == s[k]: 
                j -= 1
                k += 1
                print(j, k+1)
            resLen = k-j+1
            if maxLen < resLen:
                maxLen = resLen
                odd_res = s[j+1:k]
                print(f"Odd result: {odd_res}")
            # even case
            l = i
            r = i+1
            while l>=0 and r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
                print(l,r)
            resLen = r-l+1
            if maxLen < resLen:
                maxLen = resLen
                even_res = s[l+1:r]

        print(odd_res)
        print(even_res)
        return odd_res if len(odd_res) > len(even_res) else even_res
        


        
        
                

                    
        