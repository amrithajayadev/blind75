class Solution:
    def isHappy(self, n: int) -> bool:
        hm = set()
        def cyclical(n):
            if n==1:
                return True
            
            ss = 0
            while n > 0:
                ss += pow(n%10, 2)
                n = n//10
            if ss == 1:
                return True
            elif ss in hm:
                return False
            else:
                hm.add(ss)
                return cyclical(ss)
        return cyclical(n)
