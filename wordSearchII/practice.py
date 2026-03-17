class TrieNode(object):
    def __init__(self,isEnd=False,word=None):
        self.children={}
        self.isEnd=isEnd
        self.word=None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root=TrieNode()
        res=[]
        visited=set()
        ROW=len(board)
        COL=len(board[0])
        def addWord(word):
            curr=root
            for c in word:
                if(c not in curr.children):
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.isEnd=True
            curr.word=word
        for word in words:
            addWord(word)
        
        def dfs(curr,row,col):
            
            if(min(row,col)<0 or row==ROW or col==COL or (row,col) in visited or board[row][col] not in curr.children):
                return 
            visited.add((row,col))
            curr=curr.children[board[row][col]]
            if(curr.isEnd):
                res.append(curr.word)
                curr.isEnd=False
            dfs(curr,row+1,col)
            dfs(curr,row-1,col)
            dfs(curr,row,col+1)
            dfs(curr,row,col-1)
            visited.remove((row,col))
        for row in range(ROW):
            for col in range(COL):
                if(board[row][col] in root.children):
                    dfs(root,row,col)
        return res
            
        
            
        