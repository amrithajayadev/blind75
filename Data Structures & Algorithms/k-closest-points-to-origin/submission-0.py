class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x = point[0]
            y = point[1]
            return -1 * (x**2 + y**2)
        
        hp = [] # min heap
        for point in points:
            dist = distance(point)
            heapq.heappush(hp, (dist, point))
            if len(hp) > k:
                heapq.heappop(hp)
    
        res = []
        while hp:
            _, point = heapq.heappop(hp)
            res.append(point)
            
        return res

        