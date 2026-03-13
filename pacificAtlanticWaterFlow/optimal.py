class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        atl=set()
        pac=set()
        res=[]
        ROW=len(heights)
        COL=len(heights[0])
        def backtracking(row,col,visited,height):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited or heights[row][col]<height):
                return 
            visited.add((row,col))
            height=heights[row][col]
            backtracking(row+1,col,visited,height)
            backtracking(row-1,col,visited,height)
            backtracking(row,col+1,visited,height)
            backtracking(row,col-1,visited,height)
        for r in range(ROW):
            backtracking(r,0,pac,0)
            backtracking(r,COL-1,atl,0)
        for c in range(COL):
            backtracking(0,c,pac,0)
            backtracking(COL-1,c,atl,0)
        for row in range(ROW):
            for col in range(COL):
                if((row,col) in atl and (row,col) in pac):
                    res.append([row,col])
        return res