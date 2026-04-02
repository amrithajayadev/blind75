class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1
        output = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                output = min(output, nums[L])
                break
            mid = (L+R)//2
            output = min(output, nums[mid])
            if nums[L] <= nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return output

            
            
        
        