from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        q=deque()
        ROW=len(grid)
        COL=len(grid[0])
        def addAndVisit(row,col):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited or grid[row][col]==0):
                return 
            visited((row,col))
            q.append((row,col))
        for row in range(ROW):
            for col in range(COL):
                if(grid[row][col]==2):
                    addAndVisit(row,col)
        
        time=0
        while(q):
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=2
                addAndVisit(row+1,col)
                addAndVisit(row-1,col)
                addAndVisit(row,col+1)
                addAndVisit(row,col-1)
            time+=1
        for row in range(ROW):
            for col in range(COL):
                if(grid[row][col]==1):
                    return -1
        return time


