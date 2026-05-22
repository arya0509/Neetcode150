class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo={}
        def dfs(r,c):
            if(min(r,c)<0 or r==m or c==n):
                return 0
            if(r==m-1 and c==n-1):
                return 1
            if((r,c) in memo):
                return memo[(r,c)]
            memo[(r,c)]=dfs(r+1,c) +dfs(r,c+1)
            return memo[(r,c)]
        return dfs(0,0)
            