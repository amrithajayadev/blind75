import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_score = {}
        for i in nums:
            num_score[i] = 1 + num_score.get(i, 0)
        
        hp = []
        for key, val in num_score.items():
            # if len(hp) < k:
            #     heapq.heappush(hp, (val, key))
            # if val > hp[0][0]:
            #     heapq.heappop(hp)
            #     heapq.heappush(hp, (val, key))
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        
        output = []
        while hp:
            _, key = heapq.heappop(hp)
            output.append(key)
        return output
        