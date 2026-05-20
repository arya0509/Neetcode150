class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memo={}
        ROW=len(matrix)
        COL=len(matrix[0])
        def dfs(row,col,prev):
            if(min(row,col)<0 or row==ROW or col==COL):
                return 0
            if(matrix[row][col]==prev):
                return 0
            if((row,col) in memo):
                return memo[(row,col)]
            curr=matrix[row][col]
            if(curr<prev):
                return 0
            up=1+dfs(row-1,col,curr)
            down=1+dfs(row+1,col,curr)
            left=1+dfs(row,col-1,curr)
            right=1+dfs(row,col+1,curr)

            matrix[row][col]=max(up,down,left,right)
        maxLen=0
        for r in len(ROW):
            for c in len(COL):
                res=dfs(r,c,float("-inf"))
                maxLen=max(res,maxLen)
        return maxLen
