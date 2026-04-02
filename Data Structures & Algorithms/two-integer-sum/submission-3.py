class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            # hash_map = {n:i for i,n in enumerate(nums)}
            hash_map = {nums[j]:j for j in range(i+1, len(nums))}
            if target-n in hash_map.keys():
                return [i, hash_map[target-n]]
        return []
        
        
            



        