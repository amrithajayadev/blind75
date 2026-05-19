class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        

        for i in range(R):
            if i in rows:
                matrix[i] = [0]*C

        for j in range(C):
            for i in range(R):
                if j in cols:
                    matrix[i][j] = 0
        
        