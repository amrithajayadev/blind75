class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {} # max len of the cycles if only this particual task is present
        for t in tasks:
            mp[t] = mp.get(t, 0) + 1
        
        for t, v in mp.items():
            mp[t] = (mp[t]-1) * n + mp[t]
        print(mp)
        res = list(mp.values())
        mp_freq = {}
        for num in res:
            mp_freq[num] = 1 + mp_freq.get(num, 0)
        print(mp_freq)
        max_len = 0
        for num, freq in mp_freq.items():
            max_len = max(max_len, num + freq -1)
        return max_len if max_len > len(tasks) else len(tasks)

        