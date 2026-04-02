class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n_cost = [0] + cost
        N = len(n_cost)
        pos = 0
        min_cost = 0
        def dfs(pos):
            if pos >= N:
                return 0
            min_cost = n_cost[pos] + min(dfs(pos+1), dfs(pos+2))
            return min_cost
        

        
        def memo():
            output = [0] * (len(n_cost)+1)
            for i in range(2, len(n_cost)+1):
                output[i] = min(n_cost[i-2] + output[i-2], n_cost[i-1] + output[i-1])
            return output[-1]

        # return dfs(0)
        return memo()




        