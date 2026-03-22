from collections import deque
class Solution:
    def islandsAndTreasure(self, grid):
        visited=set()
        q=deque()
        ROW=len(grid)
        COL=len(grid[0])
        def searchAndAdd(row,col):
            if min(row,col)<0 or row==ROW or col==COL or grid[row][col]==-1 or (row,col) in visited:
                return 
            visited.add((row,col))
            q.append((row,col))
        for row in range(ROW):
            for col in range(COL):
                if(grid[row][col]==0):
                    searchAndAdd(row,col)
        dist=0
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist
                searchAndAdd(row+1,col)
                searchAndAdd(row-1,col)
                searchAndAdd(row,col+1)
                searchAndAdd(row,col-1)
            dist+=1

        