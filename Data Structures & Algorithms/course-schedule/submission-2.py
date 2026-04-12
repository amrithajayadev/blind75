class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        visited = set()
        
        def dfs(crs):
            if crs in visited: # cycle detected
                return False
            visited.add(crs)
            for c in graph[crs]:
                if not dfs(c):
                    return False
            visited.remove(crs)
            graph[crs] = []
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True