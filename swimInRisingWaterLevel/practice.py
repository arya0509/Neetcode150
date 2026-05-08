import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        heap=[(grid[0][0],0,0)]
        visited=set()
        min_time=grid[0][0]
        ROW=len(grid)
        COL=len(grid[0])
        while(heap):
            time,row,col=heapq.heappop(heap)
            if(min_time<=time):
                min_time=time
            print(time)
            if(row==ROW-1 and col==COL-1):
                return min_time
            visited.add((row,col))
            directions=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for direction in directions:
                poss_row,poss_col=direction
                if((poss_row,poss_col) in visited or poss_col>=COL or poss_row>=ROW or min(poss_row,poss_col)<0):
                    continue
                heapq.heappush(heap,(grid[poss_row][poss_col],poss_row,poss_col))
                
