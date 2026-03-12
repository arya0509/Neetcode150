from collections import deque
class Solution:
    def islandsAndTreasure(self, grid):
        q=deque()
        ROWS=len(grid)
        COLS=len(grid[0])
        visited=set()
        def add(row,col):
            if(min(row,col)<0 or row==ROWS or col==COLS or grid[row][col]==-1 or (row,col) in visited):
                return
            visited.add((row,col))
            q.append(row,col)
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col]==0):
                    q.append((row,col))
        dist=0
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist
                add(row+1,col)
                add(row-1,col)
                add(row,col+1)
                add(row,col-1)
            dist+=1

        
        