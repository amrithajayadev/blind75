class Solution:
    def climbStairs(self, n: int) -> int:
        # def climbStairs1()
        #     if n==0 or n==1:
        #         return 1
        #     return climbStairs1(n-1) + climbStairs1(n-2)
        memo = [-1]*(n+1)
        memo[0] = 1
        memo[1] = 1
        def memo1(n):
            if memo[n] != -1:
                return memo[n]
            memo[n] = memo1(n-1) + memo1(n-2)
            return memo[n]
        memo1(n)
        return memo[n]

        