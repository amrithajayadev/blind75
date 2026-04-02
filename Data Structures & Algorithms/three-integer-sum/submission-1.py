class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = list()
        nums.sort()
        i = 0
        while i < n-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i+1
            k = n-1
            while j < k:
                if nums[j]+nums[k] == nums[i]*-1:
                    output.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j]==nums[j+1]:
                        j +=1
                    while j < k and nums[k-1]==nums[k]:
                        k -=1
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] > nums[i]*-1:
                    k -= 1
                else:
                    j += 1
            i += 1
        return output
        
        