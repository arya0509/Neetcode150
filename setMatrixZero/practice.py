class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROW=len(matrix)
        COL=len(matrix[0])
        isRowZero=False
        isColZero=False
        for c in range(COL):
            if matrix[0][c]==0:
                isRowZero=True 
                break     
        for r in range(ROW):
                if matrix[r][0]==0:
                    isColZero=True
                    break
        for r in range(1,ROW):
            for c in range(1,COL):
                if(matrix[r][c]==0):
                    matrix[0][c]=0
                    matrix[r][0]=0
        for r in range(1,ROW):
            for c in range(1,COL):
                if( matrix[0][c]==0 or  matrix[r][0]==0 ):
                    matrix[r][c]=0
        if(isRowZero):
            for c in range(COL):
                matrix[0][c]=0
        if(isColZero):
            for r in range(ROW):
                matrix[r][0]=0

            
