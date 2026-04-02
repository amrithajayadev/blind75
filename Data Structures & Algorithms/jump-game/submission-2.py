class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # i = 0
        # pos = 0
        N = len(nums)-1
        # while pos <= N:
        #     pos += nums[pos]
        #     if pos >= N:
        #         return True
        #     if nums[pos] == 0 and pos < N:
        #         return False
        # return False

        goal = len(nums)-1
        for i in range(N-1, -1, -1):
            if nums[i]+ i >= goal:
                goal = i
        return goal<=0


# testcases
"""
[0]
[2,5,0,0] N=4, 
[3,2,1,0,4] N=5
[2,3,1,1,4]
"""

            

        