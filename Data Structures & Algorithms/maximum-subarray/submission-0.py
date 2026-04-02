class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2,-3,4,-2,2,1,-1,4]
        curr_sum = 0
        max_sum = -100000

        for i in range(len(nums)):
            # number itself, curr_sum + number
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

        