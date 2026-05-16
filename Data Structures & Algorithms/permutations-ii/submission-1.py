class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def perm(start):
            if start == len(nums):
                res.append(nums.copy())
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                perm(start+1)
                nums[start], nums[i] = nums[i], nums[start]
            return
        perm(0)
        return res


        