class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
       
        board=[]
        for i in range(n):
            board.append(["."]*n)
        
        def backTracking(r):
            if(r==n):
                copy=[]
                for row in board:
                     copy.append("".join(row))
                res.append(copy)
            for c in range(n):
                if(isSafe(r,c,board)):
                    board[r][c]="Q"
                    backTracking(r+1)
                    board[r][c]="."
        
        def isSafe(r,c,board):

                row=r-1
                while(row>=0):
                    if(board[row][c]=="Q"):
                          return False
                    row-=1
                
                row=r-1
                col=c-1

                while(row>=0 and col>=0):
                    if(board[row][col]=="Q"):
                          return False
                    row-=1
                    col-=1
                
                row=r-1
                col=c+1

                while(row>=0 and col<len(board)):
                    if(board[row][col]=="Q"):
                          return False
                    row-=1
                    col+=1
                
                return True
        backTracking(0)
        return res
                

