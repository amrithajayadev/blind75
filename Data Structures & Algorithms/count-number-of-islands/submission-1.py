class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        visited = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        def dfs(r,c):
            if 0<=r<R and 0<=c<C and grid[r][c]=="1" and (r,c) not in visited:
                visited.add((r,c))
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    dfs(nr,nc)
            return
        

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        return count
