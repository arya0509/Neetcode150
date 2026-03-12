class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.closing=0
        self.opening=0
        def backtrack(string):
            if(self.closing>self.opening or self.opening>n):
                return 
            if(len(string)==n*2):
                res.append(string)
                return 
            
            self.opening+=1
            backtrack(string+"(")
            self.opening-=1

            self.closing+=1
            backtrack(string+")")
            self.closing-=1
        backtrack("")
        return res