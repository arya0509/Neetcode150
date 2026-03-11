class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.maxArea=0
        def dfs(row,col,area):
            if(row<0 or col<0 or row==len(grid) or col==len(grid[0])):
                return area
            if(grid[row][col]==0):
                return area
            area=area+1
           
            grid[row][col]=0
            area=dfs(row+1,col,area)
            area=dfs(row-1,col,area)
            area=dfs(row,col+1,area)
            area=dfs(row,col-1,area)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    area=dfs(row,col,0)
                    self.maxArea=max(self.maxArea,area)
        
        return self.maxArea