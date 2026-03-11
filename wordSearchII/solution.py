from collections import defaultdict
class TrieNode(object):
    def __init__(self,isEnd=False):
        self.children={}
        self.isEnd=isEnd
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[string]]
        :type words: List[string]
        :rtype: List[string]
        """
        
        res=set()
        visited=set()
        ROWS, COLS = len(board), len(board[0])
        def backtrack(row,col,c,string):
            if(row<0 or col<0 or row==ROWS or col==COLS):
                return 
            if (row,col) in visited or board[row][col] not in c.children :
                return 
            nextNode=c.children[board[row][col]]
            string=string+board[row][col]
            if nextNode.isEnd and string not in res:
                res.add(string)
                
           
            visited.add((row,col))
            backtrack(row+1,col,nextNode,string)
            backtrack(row-1,col,nextNode,string)
            backtrack(row,col+1,nextNode,string)
            backtrack(row,col-1,nextNode,string)
            visited.remove((row,col))

            
            
            
           
        root=TrieNode()
       
        for word in words:
            curr=root
            for c in word:
                if(c not in curr.children):
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.isEnd=True
        
        curr=root      
       
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] in curr.children):
                      
                        backtrack(row,col,curr,"")
                       
        
        return list(res)
