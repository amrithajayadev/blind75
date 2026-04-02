class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(pos):
            if len(nums)==0 or pos<0:
                return 0
            return max(nums[pos]+rob1(pos-2), rob1(pos-1))
        # return rob1(len(nums)-1)
        n = len(nums)-1
        memo = [-1] * (n+1)
        memo[-1] = 0
        memo[0] = nums[0]
        for i in range(1, n+1):
            memo[i] = max(nums[i]+ memo[i-2] , memo[i-1])
        return memo[n]
