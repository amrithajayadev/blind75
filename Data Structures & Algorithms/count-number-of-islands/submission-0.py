class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        R = len(grid)
        C = len(grid[0])

        def bfs(r, c, R, C):
            if r >= R or c >=C or r<0 or c<0 or (r,c) in visited or grid[r][c]=="0":
                return False
            visited.add((r,c))
            bfs(r+1,c , R, C)
            bfs(r-1,c , R, C)
            bfs(r,c+1 , R, C)
            bfs(r,c-1 , R, C)
            return True
        
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]=="1" and (i,j) not in visited:
                    if bfs(i, j , R, C):
                        count += 1
        return count