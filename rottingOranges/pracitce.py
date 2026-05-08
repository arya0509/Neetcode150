from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        ROW=len(grid)
        COL=len(grid[0])
        self.fresh_oranges=0
        visited=set()
        def addToq(row,col):
            if(min(row,col)<0 or row>=ROW or col>=COL or grid[row][col]==0 or(row,col) in visited):
                return 
            visited.add((row,col)) 
            q.append((row,col))
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c]==1):
                    self.fresh_oranges+=1
                elif(grid[r][c]==2):
                    addToq(r,c)
      
        if(not self.fresh_oranges):
            return 0
        minTime=-1
        while(q):
            minTime+=1
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                if(grid[r][c]==1):
                    self.fresh_oranges-=1
                    grid[r][c]=2
               
                addToq(r+1,c)
                addToq(r-1,c)
                addToq(r,c+1)
                addToq(r,c-1)
           
            
        if self.fresh_oranges:
            return -1
        return minTime