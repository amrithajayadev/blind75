class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {n:i for i,n in enumerate(nums)}
        for i, n in enumerate(nums):
            if target-n in hash_map.keys():
                if i == hash_map[target-n]:
                    continue
                return [i, hash_map[target-n]]
        return []
        
        
            



        