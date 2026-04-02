from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        q = deque()
        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            r, c = q.popleft()
            # check all 4 directions and add to the queue if the cell needs to be traversed further.
            for i, j in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 2147483647:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                

        