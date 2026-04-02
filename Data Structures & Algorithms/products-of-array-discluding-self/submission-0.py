class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1,  2, 8, 48]
        # [48, 48,24, 6]
        # [48, 24, 12, 8]
    
        left = [1]*len(nums)
        right = [1]*len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i]
        print(left)

        for i in range(len(nums)-2,-1, -1):
            right[i] = right[i+1]*nums[i]
        print(right)
        output = [1]*len(nums)
        for i in range(1,len(nums)-1):
            output[i] = left[i-1] * right[i+1]
        
        output[0] = right[1]
        output[-1] = left[-2]
        return output