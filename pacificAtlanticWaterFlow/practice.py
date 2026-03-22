class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac=set()
        atl=set()
        ROW=len(heights)
        COL=len(heights[0])
        def dfs(row,col,prev,arr):
            if (min(row,col)<0 or row==ROW or col==COL or (row,col) in arr or heights[row,col]<prev):
                return 
            arr.add((row,col))
            prev=heights[row,col]
            dfs(row+1,col,prev,arr)
            dfs(row-1,col,prev,arr)
            dfs(row,col+1,prev,arr)
            dfs(row,col-1,prev,arr)
        
        for col in range(COL):
            dfs(0,col,0,pac)
            dfs(ROW-1,col,0,atl)
        for row in range(ROW):
            dfs(row,0,0,pac)
            dfs(row,COL-1,0,atl)
        res=[]
        for grid in pac:
            if(grid in atl):
                res.append(list(grid))
        return res