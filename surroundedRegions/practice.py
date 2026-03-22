class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        notRegion=set()
        ROW=len(board)
        COL=len(board[0])
        def dfs(row,col):
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in notRegion or board[row][col]=="X"):
                return 
            notRegion.add((row,col))
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for r in range(ROW):
            dfs(r,0)
            dfs(r,COL-1)
        for c in range(COL):
            dfs(0,c)
            dfs(ROW-1,c)
        for row in range(ROW):
            for col in range(COL):
                if(board[row][col]=="O" and (row,col) not in notRegion):
                    board[row][col]="X"
