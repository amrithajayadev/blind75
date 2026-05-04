class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        base case: last elem or empty list
        At each element: pick or skip

        """
        n = len(nums)-1
        res = []
        def dfs(idx, subs):
            if idx == n+1:
                res.append(subs)
                return
            
            dfs(idx+1, subs + [nums[idx]])
            dfs(idx+1, subs)
            return
        dfs(0,[])
        return res

