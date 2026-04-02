class Solution:
    def trap(self, height: List[int]) -> int:
        biggest_left = [0] * len(height)
        biggest_right = [0] * len(height)

        for i in range(1, len(height)):
            biggest_left[i] = max(height[i-1], biggest_left[i-1])

        for i in range(len(height)-2, -1, -1):
            biggest_right[i] = max(height[i+1], biggest_right[i+1])
        
        max_vol = [0] * len(height)
        for i in range(len(height)):
            area = min(biggest_left[i], biggest_right[i]) - height[i]
            max_vol[i] = area if area > 0 else 0
        return sum(max_vol)

        