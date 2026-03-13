class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS=len(board)
        COLS=len(board[0])
        visited=set()
        def backtrack(row,col,i):
            if(min(row,col)<0 or row==ROWS or col==COLS or (row,col) in visited or i==len(word)):
                  return False
            if(board[row][col]!=word[i]):
                 return False
            if(i==len(word)-1):
                 return True
            visited.add((row,col))

            up=backtrack(row-1,col,i+1)
            down=backtrack(row+1,col,i+1)
            left=backtrack(row,col-1,i+1)
            right=backtrack(row,col+1,i+1)

            visited.remove((row,col))

            return up or down or left or right 

            
            
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col]==word[0]):
                        if(backtrack(row,col,0)):
                             return True
        return False