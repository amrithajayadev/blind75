class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        max_area = 0
        while (l < r):
            area = min(heights[l], heights[r]) * (r-l)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
            max_area = max(max_area, area)
        return max_area


        