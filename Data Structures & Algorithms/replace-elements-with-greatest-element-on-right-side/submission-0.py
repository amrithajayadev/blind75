class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        for i in range(n-2,-1,-1):
            res[i] = max(res[i+1], arr[i+1])
        print(res)
        return res