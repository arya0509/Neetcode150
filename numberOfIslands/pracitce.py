class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROW=len(grid)
        COL=len(grid[0])


        def addIslandVisited(row,col):
            if(min(row,col)<0 or row>=ROW or col>=COL or grid[row][col]==0):
                return 
            grid[row][col]=0
            addIslandVisited(row+1,col)
            addIslandVisited(row-1,col)
            addIslandVisited(row,col+1)
            addIslandVisited(row,col-1)
        count=0
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c]==1):
                    count+=1
                    addIslandVisited(r,c)
        return count