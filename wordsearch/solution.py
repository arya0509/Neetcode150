class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height=len(board)
        width=len(board[0])
       
        def search(row,col,i):
           
            if row>=height or col>=width or row<0 or col<0 or i>=len(word):
                return False
          
            
            if((row,col) in hashSet or board[row][col]!=word[i]):
                return False
           
            if(board[row][col]==word[i] and (row,col) not in hashSet):
                if(i==len(word)-1):
                    return True
                hashSet.add((row,col))
                res= search(row,col+1,i+1) or search(row,col-1,i+1) or search(row+1,col,i+1) or search(row-1,col,i+1)
                hashSet.remove((row,col))
                return res
            
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col]==word[0]):
                    hashSet=set()
                    res=search(row,col,0)
                    if(res):
                        return res
        return False
          
       
                        