class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr=[]
        ROW=len(matrix)
        COL=len(matrix[0])

        for i in range(ROW):
            for j in range(COL):
                if(matrix[i][j]==0):
                    arr.append((i,j))
        for cor in arr:
            r=cor[0]
            c=cor[1]

            for i in range(COL):
                matrix[r][i]=0
            for i in range(ROW):
                matrix[i][c]=0
            
                           