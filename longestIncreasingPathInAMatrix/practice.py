class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memo={}
        m=len(matrix)
        n=len(matrix[0])
        def dfs(r,c,prev):
            if(min(r,c)<0 or r==m or c==n):
                return 0
            curr=matrix[r][c]
            if(curr<=prev):
                return 0
            if((r,c) in memo):
                return memo[(r,c)]
            
            up=dfs(r-1,c,curr)+1
            down=dfs(r+1,c,curr)+1
            left=dfs(r,c-1,curr)+1
            right=dfs(r,c+1,curr)+1
            memo[(r,c)]=max(up,down,left,right)
            return memo[(r,c)]
        res=0

        for r in range(m):
            for c in range(n):
                if((r,c) in memo):
                    val=memo[(r,c)]
                else:
                    val= dfs(r,c,float("-inf"))
                res=max(res,val)
        return res 
            