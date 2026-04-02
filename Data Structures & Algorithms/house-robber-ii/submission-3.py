class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # def rob1(pos):
        #     if pos < 0 or n==0:
        #         return 0
        #     return max(nums[pos] + rob1(pos-2), rob1(pos-1))
        # rob1(n)
        def dp_sol(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
                
            n = len(arr)-1
            memo = [-1] * (n+1)
            memo[0] = arr[0]
            memo[1] = max(arr[1], arr[0])
            for i in range(2, n+1):
                memo[i] = max(arr[i] + memo[i-2], memo[i-1])
            return memo[n]
        
        if len(nums) == 1:
            return nums[0]
        else:
            return max(dp_sol(nums[:-1]), dp_sol(nums[1:]))
        
            

        