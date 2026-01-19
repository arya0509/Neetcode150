class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[0]*9
        col=[0]*9
        square=[0]*9
        for r in range(9):
            for c in range(9):
                if(board[r][c]=="."):
                    continue

                val=int(board[r][c])-1

                if(1<<val & row[r]):
                    return False
                if(1<<val & col[c]):
                    return False
                if(1<<val & square[(r//3)*3 + (c//3)]):
                    return False
                
                row[r]=row[r] | (1<<val)
                col[c]=col[c] | (1<<val)
                square[(r//3)*3 + (c//3)]=square[(r//3)*3 + (c//3)]|(1<<val)
        return True




sol=Solution()
print(sol.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))