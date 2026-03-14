class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROW=len(board)
        COL=len(board[0])
        notRegion=set()
        def backtracking(row,col):
           if(min(row,col)<0 or row==ROW or col==COL or board[row][col]=="X" or (row,col) in notRegion):
               return 
           notRegion.add((row,col))
           backtracking(row-1,col)
           backtracking(row+1,col)
           backtracking(row,col-1)
           backtracking(row,col+1)
        
        for row in range(ROW):
            backtracking(row,0)
            backtracking(row,COL-1)
        for col in range(COL):
            backtracking(0,col)
            backtracking(ROW-1,col)
        
        for row in range(ROW):
            for col in range(COL):
                if(board[row][col]=="O" and (row,col) not in notRegion):
                    board[row][col]="X"