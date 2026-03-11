class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res=0
        def dfs(row,col):
            if(row<0 or col<0 or row==len(grid) or col==len(grid[0])):
                return 
            if(grid[row][col]==0):
                return
            grid[row][col]=0
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]==1):
                    res+=1
                    dfs(row,col)
        return res
                