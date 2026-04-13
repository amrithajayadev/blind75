class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        """
        R = len(grid)
        C = len(grid[0])

        q = deque()
        fresh = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        time = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
            
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        