class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_so_far = 0
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append([t, i])

            print(res)
        return res

        