import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency_map = {}
        for n in nums:
            num_frequency_map[n] = 1 + num_frequency_map.get(n,0)
        
        hp = []
        for key, val in num_frequency_map.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        
        output = []
        for _, key in hp:
            output.append(key)
        return output
            
        
        