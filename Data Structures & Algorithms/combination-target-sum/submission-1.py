class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        n = len(nums)
        def combination(start, c, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                output.append(c[:])
                return
            for i in range(start,n):
                if cur_sum + nums[i] <= target: 
                    combination(i, c + [nums[i]], cur_sum+nums[i])
        
        for i in range(n):
            combination(i, [nums[i]], nums[i])
        return output

        