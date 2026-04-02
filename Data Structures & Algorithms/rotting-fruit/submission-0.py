class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS v/s DFS
        BFS for shortest path. At each level, shortest path is traversed. Num levels = time
        DFS will explore the path complately 
        and may not always be the shortest path. Will need to keep DFSing on each point. not optimal
        """

        R = len(grid)
        C = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1), (0,-1)]
        q = deque()
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while q and fresh:
            length = len(q)
            for k in range(length):
                r, c = q.popleft()
                for i ,j in dirs:
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==1:
                        fresh -= 1
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            time += 1
        return time if fresh==0 else -1


        