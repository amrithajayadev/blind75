class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [1000000] * (n+1)
        min_time[k] = 0
        min_time[0] = 0
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v,t))
        
        res = 0
        q = deque()
        q.append((k,0))
        while q:
            size = len(q)
            for _ in range(size):
                src, ti = q.popleft()
                for d,t in graph[src]:
                    nt = ti + t
                    if min_time[d] > nt:
                        min_time[d] = nt
                        q.append((d,nt))
            res += 1
        max_time = max(min_time)
        return max_time if max_time != 1000000 else -1
            
