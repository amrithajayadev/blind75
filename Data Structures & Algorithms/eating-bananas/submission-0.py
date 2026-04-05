class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        lo = 1
        hi = sum(piles)

        def canEat(n):
            total = 0
            for p in piles:
                hrs = math.ceil(p/n) if p > n else 1 
                total += hrs
                if total > h:
                    return False
            return True

        while lo <= hi:
            mid = (hi+lo)//2
            if canEat(mid):
                hi = mid-1
            else:
                lo = mid + 1
        
        return lo