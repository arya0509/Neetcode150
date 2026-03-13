class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        atlanticPoints=set()
        res=[]
        visited=set()
        ROW=len(heights)
        COL=len(heights[0])
        def backtrackAt(row,col,height):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited or (row,col) in atlanticPoints):
                return 
            if(heights[row][col]<height):
                return
            atlanticPoints.add((row,col))
            visited.add((row,col))
            height=heights[row][col]
            backtrackAt(row+1,col,height)
            backtrackAt(row-1,col,height)
            backtrackAt(row,col+1,height)
            backtrackAt(row,col-1,height)
            visited.remove((row,col))
        def backtrackPa(row,col,height):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited or [row,col] in res):
                return 
            if(heights[row][col]<height):
                return
            if((row,col) in atlanticPoints):
                res.append([row,col])
            visited.add((row,col))
            height=heights[row][col]
            backtrackPa(row+1,col,height)
            backtrackPa(row-1,col,height)
            backtrackPa(row,col+1,height)
            backtrackPa(row,col-1,height)
            visited.remove((row,col))

        for row in range(ROW):
            backtrackAt(row,COL-1,0)
        for col in range(COL-1):
            backtrackAt(ROW-1,col,0)
        
        for col in range(COL):
            backtrackPa(0,col,0)
        for row in range(1,ROW):
            backtrackPa(row,0,0)
        
        return res