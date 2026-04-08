class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n # greatest element towards left
        suffix = [0] * n # greatest element to right
        prefix[0] = height[0]
        suffix[n-1] = height[n-1]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1], height[i])
        print(prefix)
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        print(suffix)
        vol = [0] * n
        for i in range(n):
            vol[i] = min(prefix[i], suffix[i]) - height[i]
        print(vol)
        return sum(vol)