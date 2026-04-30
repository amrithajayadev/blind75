class TrieNode:
    def __init__(self):
        self.children = {}
        self.last_char = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.last_char = True
        
        R = len(board)
        C = len(board[0])
        visited = set()
        res = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r, c, s, node):
            if node.last_char:
                res.add(s)
            visited.add((r,c)) 
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in visited and board[nr][nc] in node.children:
                    new_node = node.children[board[nr][nc]]
                    dfs(nr,nc,s+board[nr][nc], new_node)
            visited.remove((r,c))
            return

        for i in range(R):
            for j in range(C):
                if (i,j) not in visited and board[i][j] in root.children:
                    dfs(i, j,board[i][j], root.children[board[i][j]])

        return list(res)       

        