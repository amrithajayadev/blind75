class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. Scan the board for word[0]
        2. DFS on the board to find the next char. If not return False
        3. Stop DFS when the word is found
        """

        R = len(board)
        C = len(board[0])
        visited = set()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r,c,s,k):
            if s==word:
                return True
            if (r,c) in visited or k > len(word):
                return False
            visited.add((r,c))
            for dr,dc in dirs:
                nr = r+dr
                nc = c + dc
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in visited and board[nr][nc]==word[k+1]:
                    if dfs(nr,nc,s+board[nr][nc], k+1):
                        return True
            visited.remove((r,c))
            return False


        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and (i,j) not in visited:
                    if dfs(i,j,word[0],0):
                        return True
        return False

