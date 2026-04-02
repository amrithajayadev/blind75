class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        # [3,4,5,6,1,2]
        # [5,6,1,2,3,4]
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] == target:
                return mid
            # left sorted side
            # if the left is bigger than the target, 
            # if the mid is smaller than the target,
            # then search in the right side.
            if nums[L] <= nums[mid]:
                if nums[L] > target or nums[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                if nums[mid] > target or nums[R] < target:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1




            
            
        
        