class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        rev = defaultdict(set)
        for c1, c2 in prerequisites:
            graph[c1].add(c2)
            rev[c2].add(c1)

        indegrees = [0] * numCourses
        for c, v in graph.items():
            indegrees[c] = len(v)
        
        q = deque()
        for crs, ind in enumerate(indegrees):
            if ind == 0:
                q.append(crs)
        
        output = []
        while q:
            crs = q.popleft()
            output.append(crs)
            for c in rev[crs]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    q.append(c)
            if len(output)==numCourses:
                return output
        if sum(indegrees) > 0: 
            return [] 
        else:
            return output


        