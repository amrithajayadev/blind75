import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.length = len(nums)
        self.nums = nums
        self.hp = []
        for n in self.nums:
            heapq.heappush(self.hp, n)
            if len(self.hp) > k:
                heapq.heappop(self.hp)  
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
        
