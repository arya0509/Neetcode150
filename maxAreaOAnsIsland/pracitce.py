class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max=0
        ROW=len(grid)
        COL=len(grid[0])

        def dfs(row,col):
            if(min(row,col)<0 or row==ROW or col==COL or grid[row][col]==0):
                return 0
            grid[row][col]=0
            up=dfs(row-1,col)
            down=dfs(row+1,col)
            left=dfs(row,col-1)
            right=dfs(row,col+1)

            return 1 + up+down+left+right
        for row in range(ROW):
            for col in range(COL):
                if(grid[row][col]==1):
                    self.max=max(self.max,dfs(row,col))
        return self.max

