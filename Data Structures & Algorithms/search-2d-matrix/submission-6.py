class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        # Narrow down on the row by looking at the last values of each row
        lo = 0
        hi = R-1

        while lo <= hi:
            mid = (lo+hi)//2
            if target <= matrix[mid][C-1]:
                hi = mid - 1
            else:
                lo = mid + 1
        print(lo, hi)
        l = 0
        h = C-1
        if lo>=R:
            return False

        while l <= h:
            m = (l+h)//2
            if target == matrix[lo][m]:
                return True
            elif target < matrix[lo][m]:
                h = m - 1
            else:
                l = m + 1
        return False
    
        