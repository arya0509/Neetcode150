from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        freshOranges={"n":0}
        visited=set()
        q=deque()
        mins=-1
        ROWS=len(grid)
        COLS=len(grid[0])
        def add(row,col):
            if(min(row,col)<0 or row==ROWS or col==COLS):
                return 
            if((row,col) in visited or grid[row][col]==0):
                return
            visited.add((row,col))
            q.append((row,col))
            # print([row,col])
        
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col]==1):
                    freshOranges["n"]+=1
                elif(grid[row][col]==2):
                    add(row,col)
        while(q):
            mins+=1
            for i in range(len(q)):
                r,c=q.popleft()
                if(grid[r][c]==1):
                    freshOranges["n"]-=1
                   
                    grid[r][c]=2
               
                add(r+1,c)
                add(r-1,c)
                add(r,c+1)
                add(r,c-1)
        
        if(freshOranges["n"]!=0):
            
            return -1
        if(mins==-1):
                return 0
        return mins
                
                
        
        
