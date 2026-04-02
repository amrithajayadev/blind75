class Solution:
    def check_circuit(self, idx, arr):
        i = idx
        curr_sum = 0
        total_covered = 0
        while total_covered < len(arr):
            i = idx
            while i < len(arr): 
                curr_sum += arr[i]
                if curr_sum < 0:
                    return curr_sum
                i += 1
                total_covered += 1
            i = 0
            while i < idx:
                curr_sum += arr[i]
                if curr_sum < 0:
                    return curr_sum
                i += 1
                total_covered += 1
        return idx
                
        


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g,c in zip(gas, cost)]
        max_pos = 0
        max_val = 0
        if sum(diff) < 0:
            return -1
        for i, d in enumerate(diff):
            if d >= 0:
                if self.check_circuit(i, diff) >= 0:
                    return self.check_circuit(i, diff)
        return -1
            

        