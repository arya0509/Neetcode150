class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vertical={
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[]
        }
        horizontal={
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[]
        }
        matrix={
            (3,3):[],
            (6,3):[],
            (9,3):[],
            (3,6):[],
            (6,6):[],
            (9,6):[],
            (3,9):[],
            (6,9):[],
            (9,9):[]
        }


        for i in range(len(board)):
            for row in range(len(board[i])):
                if(board[i][row]=="."):
                    continue
                if board[i][row] in vertical[row+1]:
                    print("false veritcal")

                    return False
                vertical[row+1].append(board[i][row])

                if board[i][row] in board[i][row+1:len(board[i])]:
                    print("false hori")

                    return False
                horizontal[i+1].append(board[i][row])

                for tup in sorted(matrix.keys()):
                   
                    if(tup[0]>=row+1 and tup[1]>=i+1):
                        
                        if board[i][row] in matrix[tup]:
                            
                            return False
                        
                        matrix[tup].append(board[i][row])
                        break
        return True

sol=Solution()
print(sol.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))