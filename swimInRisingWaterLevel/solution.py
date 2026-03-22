from collections import deque
import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
       
        heap=[(grid[0][0],0,0)]
        visited=set()
        ROW=len(grid)
        COL=len(grid[0])
        def addAndVisit(row,col):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited):
                return 
            heapq.heappush(heap,(grid[row][col],row,col))
            visited.add((row,col))
        maxVal=grid[0][0]
        t=0
        while heap:
            for i in range(len(heap)):
                val,row,col=heapq.heappop(heap)
                if(row==ROW-1 and col==COL-1):
                    maxVal=max(maxVal,val)
                    return maxVal
                if(t<val):
                    t=val
                maxVal=max(maxVal,val)
                addAndVisit(row+1,col)
                addAndVisit(row-1,col)
                addAndVisit(row,col+1)
                addAndVisit(row,col-1)
            t+=1
       

                

