import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [n*-1 for n in stones]
        heapq.heapify(hp)
        x = -1
        y = -1
        while len(hp) >= 2:
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            if y > x:
                heapq.heappush(hp, x-y)
            print( x, y, x-y)
        print(hp)
        if len(hp)==2:
            return hp[0]-hp[1]
        elif len(hp)==1:
            return hp[0] * -1
        else:
            return 0
            
            
        