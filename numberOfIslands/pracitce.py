class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.count=0
       
        ROW=len(grid)
        COL=len(grid[0])

        def dfs(row,col):
            if(min(row,col)<0 or row==ROW or col==COL or grid[row][col]=="0" ):
                return 
            grid[row][col]="0"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        
        for row in range(ROW):
            for col in range(COL):
                if(grid[row][col]=="1"):
                    dfs(row,col)
                    self.count+=1
        return self.count