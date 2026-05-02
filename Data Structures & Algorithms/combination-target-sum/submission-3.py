class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        backtracking solution
        same idx allowed
        add 
        dfs
        remove
        """

        res = []
        n = len(nums)
        def dfs(start, comb, cur_sum):
            if cur_sum == target:
                res.append(comb[:])
            if cur_sum > target:
                return
            for i in range(start, n):
                comb.append(nums[i])
                dfs(i, comb, cur_sum + nums[i])
                comb.pop()
            return
        dfs(0,[],0)
        return res